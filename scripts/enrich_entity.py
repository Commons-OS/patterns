#!/usr/bin/env python3
"""
Entity Enrichment Script for Commons OS Pattern Engine

Usage:
    python3 enrich_entity.py <entity_file.md>
    python3 enrich_entity.py --all-staging          # Enrich all staging entities
    python3 enrich_entity.py --build-embeddings     # Build/update embedding index

This script uses AI to:
1. Check content quality and completeness
2. Suggest refined tags based on content analysis
3. Discover relationships to other patterns and lighthouses

Requires: OPENAI_API_KEY environment variable
"""

import sys
import os
import json
import yaml
import re
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple

# Check for OpenAI
try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False
    print("Warning: openai package not installed. AI features disabled.")

# Constants
EMBEDDING_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4.1-mini"
EMBEDDING_INDEX_PATH = "data/embeddings.json"
MAX_SIMILAR_ENTITIES = 10
SIMILARITY_THRESHOLD = 0.7


def get_openai_client():
    """Get OpenAI client if available."""
    if not HAS_OPENAI:
        return None
    return OpenAI()


def parse_frontmatter(content: str) -> Tuple[Optional[Dict], str]:
    """Extract YAML frontmatter and body from markdown content."""
    if not content.startswith('---'):
        return None, content
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, content
    
    try:
        frontmatter = yaml.safe_load(parts[1])
        body = parts[2]
        return frontmatter, body
    except yaml.YAMLError:
        return None, content


def get_embedding(client, text: str) -> List[float]:
    """Get embedding vector for text."""
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text[:8000]  # Truncate to avoid token limits
    )
    return response.data[0].embedding


def cosine_similarity(a: List[float], b: List[float]) -> float:
    """Calculate cosine similarity between two vectors."""
    import math
    dot_product = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0
    return dot_product / (norm_a * norm_b)


def load_embedding_index(base_dir: Path) -> Dict:
    """Load the embedding index from disk."""
    index_path = base_dir / EMBEDDING_INDEX_PATH
    if index_path.exists():
        with open(index_path, 'r') as f:
            return json.load(f)
    return {"version": "1.0", "entities": {}}


def save_embedding_index(base_dir: Path, index: Dict):
    """Save the embedding index to disk."""
    index_path = base_dir / EMBEDDING_INDEX_PATH
    index_path.parent.mkdir(parents=True, exist_ok=True)
    with open(index_path, 'w') as f:
        json.dump(index, f, indent=2)


def build_embeddings(base_dir: Path, client) -> Dict:
    """Build or update embedding index for all entities."""
    print("Building embedding index...")
    index = load_embedding_index(base_dir)
    
    entities_processed = 0
    for subdir in ['_patterns', '_lighthouses']:
        dir_path = base_dir / subdir
        if not dir_path.exists():
            continue
        
        for filepath in dir_path.glob('*.md'):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            frontmatter, body = parse_frontmatter(content)
            if not frontmatter or 'id' not in frontmatter:
                continue
            
            entity_id = frontmatter['id']
            
            # Skip if already indexed and file hasn't changed
            file_mtime = os.path.getmtime(filepath)
            if entity_id in index['entities']:
                if index['entities'][entity_id].get('mtime', 0) >= file_mtime:
                    continue
            
            # Create embedding text from title + body
            title = frontmatter.get('title', '')
            embedding_text = f"{title}\n\n{body[:4000]}"
            
            print(f"  Embedding: {title[:50]}...")
            embedding = get_embedding(client, embedding_text)
            
            index['entities'][entity_id] = {
                'title': title,
                'slug': frontmatter.get('slug', ''),
                'type': 'pattern' if entity_id.startswith('pat_') else 'lighthouse',
                'embedding': embedding,
                'mtime': file_mtime
            }
            entities_processed += 1
    
    save_embedding_index(base_dir, index)
    print(f"Indexed {entities_processed} new/updated entities. Total: {len(index['entities'])}")
    return index


def find_similar_entities(entity_id: str, embedding: List[float], index: Dict, top_k: int = MAX_SIMILAR_ENTITIES) -> List[Dict]:
    """Find the most similar entities based on embedding similarity."""
    similarities = []
    
    for other_id, other_data in index['entities'].items():
        if other_id == entity_id:
            continue
        
        similarity = cosine_similarity(embedding, other_data['embedding'])
        if similarity >= SIMILARITY_THRESHOLD:
            similarities.append({
                'id': other_id,
                'title': other_data['title'],
                'type': other_data['type'],
                'similarity': round(similarity, 3)
            })
    
    similarities.sort(key=lambda x: x['similarity'], reverse=True)
    return similarities[:top_k]


def check_quality(client, content: str, entity_type: str) -> Dict:
    """Use AI to check content quality and completeness."""
    prompt = f"""Analyze this {entity_type} documentation for quality and completeness.

Content:
{content[:6000]}

Evaluate on these criteria (score 1-5 each):
1. Clarity: Is the writing clear and understandable?
2. Completeness: Are all sections adequately filled?
3. Accuracy: Do the claims seem well-supported?
4. 7 Pillars Justification: Are the pillar scores well-justified?
5. Actionability: Can someone implement this based on the content?

Respond in JSON format:
{{
    "scores": {{
        "clarity": <1-5>,
        "completeness": <1-5>,
        "accuracy": <1-5>,
        "pillars_justification": <1-5>,
        "actionability": <1-5>
    }},
    "overall_score": <1-5>,
    "issues": ["list of specific issues found"],
    "suggestions": ["list of improvement suggestions"]
}}"""

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )
    
    return json.loads(response.choices[0].message.content)


def suggest_tags(client, content: str, frontmatter: Dict, entity_type: str) -> Dict:
    """Use AI to suggest refined tags based on content analysis."""
    current_tags = frontmatter.get('tags', {})
    
    prompt = f"""Analyze this {entity_type} and suggest appropriate tags.

Title: {frontmatter.get('title', 'Unknown')}
Current tags: {json.dumps(current_tags, indent=2)}

Content:
{content[:4000]}

Based on the content, suggest tags for:
- domain: governance, operations, finance, technology, culture, security, privacy, sovereignty, startup
- category: specific subcategories within the domain
- era: pre-industrial, industrial, cognitive
- commons_alignment: 1-5 score with justification

Respond in JSON format:
{{
    "suggested_tags": {{
        "domain": "<suggested domain>",
        "category": ["<category1>", "<category2>"],
        "era": ["<era>"],
        "commons_alignment": <1-5>
    }},
    "tag_changes": ["list of recommended tag changes with reasons"],
    "alignment_justification": "explanation for commons_alignment score"
}}"""

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )
    
    return json.loads(response.choices[0].message.content)


def suggest_relationships(client, content: str, frontmatter: Dict, similar_entities: List[Dict]) -> Dict:
    """Use AI to suggest relationships based on content and similar entities."""
    
    similar_list = "\n".join([
        f"- {e['id']}: {e['title']} (similarity: {e['similarity']})"
        for e in similar_entities
    ])
    
    prompt = f"""Analyze this pattern/lighthouse and suggest relationships to other entities.

Title: {frontmatter.get('title', 'Unknown')}
ID: {frontmatter.get('id', 'Unknown')}

Content excerpt:
{content[:3000]}

Similar entities found (by semantic similarity):
{similar_list}

Suggest relationships of these types:
- generalizes_from: This is a more general form of...
- specializes_to: This is specialized by...
- enables: This enables...
- requires: This requires...
- related: Related to...

Respond in JSON format:
{{
    "suggested_relationships": {{
        "generalizes_from": ["{{"id": "...", "reason": "..."}}"],
        "specializes_to": ["{{"id": "...", "reason": "..."}}"],
        "enables": ["{{"id": "...", "reason": "..."}}"],
        "requires": ["{{"id": "...", "reason": "..."}}"],
        "related": ["{{"id": "...", "reason": "..."}}"]
    }},
    "confidence": "high/medium/low",
    "notes": "any additional observations"
}}"""

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )
    
    return json.loads(response.choices[0].message.content)


def enrich_entity(filepath: str, base_dir: Path) -> Dict:
    """Run full enrichment pipeline on an entity."""
    client = get_openai_client()
    if not client:
        return {"error": "OpenAI client not available"}
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    frontmatter, body = parse_frontmatter(content)
    if not frontmatter:
        return {"error": "Could not parse frontmatter"}
    
    entity_id = frontmatter.get('id', 'unknown')
    entity_type = 'pattern' if entity_id.startswith('pat_') else 'lighthouse'
    
    print(f"Enriching: {frontmatter.get('title', filepath)}")
    
    # Load or build embedding index
    index = load_embedding_index(base_dir)
    
    # Get embedding for this entity
    title = frontmatter.get('title', '')
    embedding_text = f"{title}\n\n{body[:4000]}"
    embedding = get_embedding(client, embedding_text)
    
    # Find similar entities
    print("  Finding similar entities...")
    similar = find_similar_entities(entity_id, embedding, index)
    
    # Run quality check
    print("  Checking quality...")
    quality = check_quality(client, content, entity_type)
    
    # Suggest tags
    print("  Analyzing tags...")
    tags = suggest_tags(client, content, frontmatter, entity_type)
    
    # Suggest relationships
    print("  Discovering relationships...")
    relationships = suggest_relationships(client, content, frontmatter, similar)
    
    # Compile enrichment report
    report = {
        "entity_id": entity_id,
        "entity_title": frontmatter.get('title', 'Unknown'),
        "entity_type": entity_type,
        "filepath": str(filepath),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "quality": quality,
        "tags": tags,
        "relationships": relationships,
        "similar_entities": similar
    }
    
    # Save report
    report_dir = base_dir / "data" / "enrichment_reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / f"{entity_id}.json"
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"  Report saved: {report_path}")
    
    return report


def print_enrichment_summary(report: Dict):
    """Print a human-readable summary of the enrichment report."""
    print("\n" + "="*60)
    print(f"ENRICHMENT REPORT: {report['entity_title']}")
    print("="*60)
    
    # Quality
    q = report.get('quality', {})
    print(f"\n📊 QUALITY SCORE: {q.get('overall_score', 'N/A')}/5")
    if 'scores' in q:
        for k, v in q['scores'].items():
            print(f"   - {k}: {v}/5")
    if q.get('issues'):
        print("\n⚠️ Issues:")
        for issue in q['issues'][:3]:
            print(f"   - {issue}")
    
    # Tags
    t = report.get('tags', {})
    if t.get('tag_changes'):
        print("\n🏷️ TAG SUGGESTIONS:")
        for change in t['tag_changes'][:3]:
            print(f"   - {change}")
    
    # Relationships
    r = report.get('relationships', {})
    if r.get('suggested_relationships'):
        print("\n🔗 RELATIONSHIP SUGGESTIONS:")
        for rel_type, rels in r['suggested_relationships'].items():
            if rels:
                print(f"   {rel_type}:")
                for rel in rels[:2]:
                    if isinstance(rel, dict):
                        print(f"      - {rel.get('id', 'unknown')}: {rel.get('reason', '')[:50]}")
    
    # Similar entities
    if report.get('similar_entities'):
        print("\n🔍 SIMILAR ENTITIES:")
        for e in report['similar_entities'][:5]:
            print(f"   - {e['title'][:40]} ({e['similarity']})")
    
    print("\n" + "="*60)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent
    
    if sys.argv[1] == '--build-embeddings':
        client = get_openai_client()
        if not client:
            print("Error: OpenAI client required for building embeddings")
            sys.exit(1)
        build_embeddings(base_dir, client)
        sys.exit(0)
    
    elif sys.argv[1] == '--all-staging':
        staging_dirs = [
            base_dir / '_staging' / 'patterns',
            base_dir / '_staging' / 'lighthouses'
        ]
        for staging_dir in staging_dirs:
            if staging_dir.exists():
                for filepath in staging_dir.glob('*.md'):
                    report = enrich_entity(str(filepath), base_dir)
                    print_enrichment_summary(report)
    
    else:
        filepath = sys.argv[1]
        report = enrich_entity(filepath, base_dir)
        print_enrichment_summary(report)


if __name__ == '__main__':
    main()

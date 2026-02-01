#!/usr/bin/env python3
"""
Duplication Detection Script for Commons OS Pattern Engine

Usage:
    python3 check_duplicates.py <entity_file.md>           # Check single file
    python3 check_duplicates.py --all-staging              # Check all staging files
    python3 check_duplicates.py --rebuild-index            # Rebuild similarity index

This script detects potential duplicates by:
1. Title similarity (fuzzy matching)
2. Content similarity (embedding-based)
3. Tag overlap analysis

Thresholds:
- >95% similarity: BLOCK - Almost certainly a duplicate
- 85-95% similarity: REVIEW - Likely duplicate, needs manual review
- 70-85% similarity: LINK - May be related, suggest relationship
- <70% similarity: PASS - Probably unique

Requires: OPENAI_API_KEY environment variable for embedding-based checks
"""

import sys
import os
import json
import yaml
import re
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple
from difflib import SequenceMatcher

# Check for OpenAI
try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

# Constants
EMBEDDING_MODEL = "text-embedding-3-small"
SIMILARITY_INDEX_PATH = "data/similarity_index.json"

# Thresholds
BLOCK_THRESHOLD = 0.95      # Almost certainly a duplicate
REVIEW_THRESHOLD = 0.85     # Likely duplicate, needs review
LINK_THRESHOLD = 0.70       # May be related, suggest link


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


def normalize_title(title: str) -> str:
    """Normalize title for comparison."""
    # Remove common prefixes/suffixes, lowercase, remove special chars
    title = title.lower()
    title = re.sub(r'^(the|a|an)\s+', '', title)
    title = re.sub(r'\s+(pattern|model|framework|method|approach)$', '', title)
    title = re.sub(r'[^\w\s]', '', title)
    title = re.sub(r'\s+', ' ', title).strip()
    return title


def title_similarity(title1: str, title2: str) -> float:
    """Calculate title similarity using fuzzy matching."""
    norm1 = normalize_title(title1)
    norm2 = normalize_title(title2)
    return SequenceMatcher(None, norm1, norm2).ratio()


def tag_overlap(tags1: Dict, tags2: Dict) -> float:
    """Calculate tag overlap between two entities."""
    def flatten_tags(tags):
        flat = set()
        for key, value in tags.items():
            if isinstance(value, list):
                flat.update(str(v).lower() for v in value)
            elif isinstance(value, str):
                flat.add(value.lower())
        return flat
    
    set1 = flatten_tags(tags1)
    set2 = flatten_tags(tags2)
    
    if not set1 or not set2:
        return 0.0
    
    intersection = set1 & set2
    union = set1 | set2
    return len(intersection) / len(union)


def cosine_similarity(a: List[float], b: List[float]) -> float:
    """Calculate cosine similarity between two vectors."""
    import math
    dot_product = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0
    return dot_product / (norm_a * norm_b)


def get_embedding(client, text: str) -> List[float]:
    """Get embedding vector for text."""
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text[:8000]
    )
    return response.data[0].embedding


def load_similarity_index(base_dir: Path) -> Dict:
    """Load the similarity index from disk."""
    index_path = base_dir / SIMILARITY_INDEX_PATH
    if index_path.exists():
        with open(index_path, 'r') as f:
            return json.load(f)
    return {"version": "1.0", "entities": {}}


def save_similarity_index(base_dir: Path, index: Dict):
    """Save the similarity index to disk."""
    index_path = base_dir / SIMILARITY_INDEX_PATH
    index_path.parent.mkdir(parents=True, exist_ok=True)
    with open(index_path, 'w') as f:
        json.dump(index, f, indent=2)


def build_similarity_index(base_dir: Path, client=None) -> Dict:
    """Build or update similarity index for all canonical entities."""
    print("Building similarity index...")
    index = {"version": "1.0", "entities": {}}
    
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
            title = frontmatter.get('title', '')
            tags = frontmatter.get('tags', {})
            
            entry = {
                'title': title,
                'normalized_title': normalize_title(title),
                'tags': tags,
                'filepath': str(filepath.relative_to(base_dir)),
                'type': 'pattern' if entity_id.startswith('pat_') else 'lighthouse'
            }
            
            # Add embedding if OpenAI is available
            if client:
                embedding_text = f"{title}\n\n{body[:2000]}"
                print(f"  Embedding: {title[:40]}...")
                entry['embedding'] = get_embedding(client, embedding_text)
            
            index['entities'][entity_id] = entry
    
    save_similarity_index(base_dir, index)
    print(f"Indexed {len(index['entities'])} entities")
    return index


def check_duplicates(filepath: str, base_dir: Path) -> Dict:
    """Check a file for potential duplicates."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    frontmatter, body = parse_frontmatter(content)
    if not frontmatter:
        return {"error": "Could not parse frontmatter", "status": "ERROR"}
    
    new_id = frontmatter.get('id', 'unknown')
    new_title = frontmatter.get('title', '')
    new_tags = frontmatter.get('tags', {})
    
    print(f"Checking: {new_title}")
    
    # Load index
    index = load_similarity_index(base_dir)
    if not index['entities']:
        print("  No existing entities to compare against")
        return {
            "status": "PASS",
            "reason": "No existing entities in index",
            "candidates": []
        }
    
    # Get embedding for new entity if OpenAI available
    client = get_openai_client()
    new_embedding = None
    if client:
        embedding_text = f"{new_title}\n\n{body[:2000]}"
        new_embedding = get_embedding(client, embedding_text)
    
    # Check against all existing entities
    candidates = []
    
    for entity_id, entity_data in index['entities'].items():
        if entity_id == new_id:
            continue
        
        # Title similarity
        title_sim = title_similarity(new_title, entity_data['title'])
        
        # Tag overlap
        tag_sim = tag_overlap(new_tags, entity_data.get('tags', {}))
        
        # Content similarity (if embeddings available)
        content_sim = 0.0
        if new_embedding and 'embedding' in entity_data:
            content_sim = cosine_similarity(new_embedding, entity_data['embedding'])
        
        # Combined score (weighted average)
        if new_embedding and 'embedding' in entity_data:
            combined = (title_sim * 0.3) + (content_sim * 0.5) + (tag_sim * 0.2)
        else:
            combined = (title_sim * 0.6) + (tag_sim * 0.4)
        
        if combined >= LINK_THRESHOLD:
            candidates.append({
                'id': entity_id,
                'title': entity_data['title'],
                'filepath': entity_data['filepath'],
                'scores': {
                    'title': round(title_sim, 3),
                    'content': round(content_sim, 3),
                    'tags': round(tag_sim, 3),
                    'combined': round(combined, 3)
                }
            })
    
    # Sort by combined score
    candidates.sort(key=lambda x: x['scores']['combined'], reverse=True)
    
    # Determine status
    if candidates:
        top_score = candidates[0]['scores']['combined']
        if top_score >= BLOCK_THRESHOLD:
            status = "BLOCK"
            reason = f"Almost certainly a duplicate of '{candidates[0]['title']}' ({top_score:.1%} similarity)"
        elif top_score >= REVIEW_THRESHOLD:
            status = "REVIEW"
            reason = f"Likely duplicate of '{candidates[0]['title']}' ({top_score:.1%} similarity) - manual review required"
        else:
            status = "LINK"
            reason = f"May be related to '{candidates[0]['title']}' ({top_score:.1%} similarity) - consider adding relationship"
    else:
        status = "PASS"
        reason = "No similar entities found"
    
    result = {
        "entity_id": new_id,
        "entity_title": new_title,
        "status": status,
        "reason": reason,
        "candidates": candidates[:5],  # Top 5 candidates
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    
    # Save report
    report_dir = base_dir / "data" / "duplicate_reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / f"{new_id}.json"
    with open(report_path, 'w') as f:
        json.dump(result, f, indent=2)
    
    return result


def print_result(result: Dict):
    """Print duplication check result."""
    status_icons = {
        "BLOCK": "🚫",
        "REVIEW": "⚠️",
        "LINK": "🔗",
        "PASS": "✅",
        "ERROR": "❌"
    }
    
    icon = status_icons.get(result['status'], "❓")
    
    print("\n" + "="*60)
    print(f"{icon} DUPLICATION CHECK: {result['status']}")
    print("="*60)
    print(f"Entity: {result.get('entity_title', 'Unknown')}")
    print(f"Reason: {result.get('reason', 'N/A')}")
    
    if result.get('candidates'):
        print("\nSimilar entities found:")
        for i, c in enumerate(result['candidates'][:5], 1):
            scores = c['scores']
            print(f"  {i}. {c['title']}")
            print(f"     Combined: {scores['combined']:.1%} | Title: {scores['title']:.1%} | Content: {scores['content']:.1%}")
    
    print("="*60)
    
    # Return exit code based on status
    if result['status'] == 'BLOCK':
        return 2
    elif result['status'] == 'REVIEW':
        return 1
    return 0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent
    
    if sys.argv[1] == '--rebuild-index':
        client = get_openai_client()
        build_similarity_index(base_dir, client)
        sys.exit(0)
    
    elif sys.argv[1] == '--all-staging':
        exit_code = 0
        staging_dirs = [
            base_dir / '_staging' / 'patterns',
            base_dir / '_staging' / 'lighthouses'
        ]
        for staging_dir in staging_dirs:
            if staging_dir.exists():
                for filepath in staging_dir.glob('*.md'):
                    result = check_duplicates(str(filepath), base_dir)
                    code = print_result(result)
                    exit_code = max(exit_code, code)
        sys.exit(exit_code)
    
    else:
        filepath = sys.argv[1]
        result = check_duplicates(filepath, base_dir)
        exit_code = print_result(result)
        sys.exit(exit_code)


if __name__ == '__main__':
    main()

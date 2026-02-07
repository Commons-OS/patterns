#!/usr/bin/env python3
"""
Build all indexes for the Commons OS Pattern Engine.

This single script generates all required index files from the source patterns:
- search-index.json: Frontend search functionality
- graph.json: Knowledge graph with relationships
- registry.json: TypeID to pattern mapping (used by Jekyll templates)
- _data/pattern_index_lite.json: Compact index for ChatGPT GPT Actions API

Run: python3 scripts/build_indexes.py

Updated: 2026-02-02 - Support for multi-value commons_domain arrays (ADR-012)
"""

import json
import re
import yaml
from datetime import datetime, date
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any


# Configuration
REPO_ROOT = Path(__file__).parent.parent
PATTERNS_DIR = REPO_ROOT / "_patterns"
LIGHTHOUSES_DIR = REPO_ROOT / "_lighthouses"
OUTPUT_DIR = REPO_ROOT / "data"
SEARCH_INDEX_PATH = REPO_ROOT / "search-index.json"
REGISTRY_PATH = REPO_ROOT / "_data" / "registry.json"
LITE_INDEX_PATH = REPO_ROOT / "_data" / "pattern_index_lite.json"


def parse_frontmatter(filepath: Path) -> Tuple[Optional[Dict], str]:
    """Parse YAML frontmatter from a markdown file."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  Warning: Could not read {filepath}: {e}")
        return None, ""
    
    if not content.startswith('---'):
        return None, content
    
    try:
        # Find the closing ---
        end_match = re.search(r'\n---\s*\n', content[3:])
        if not end_match:
            return None, content
        
        yaml_content = content[3:end_match.start() + 3]
        body = content[end_match.end() + 3:]
        
        frontmatter = yaml.safe_load(yaml_content)
        return frontmatter, body
    except yaml.YAMLError as e:
        print(f"  Warning: YAML error in {filepath}: {e}")
        return None, content


def json_serializer(obj: Any) -> Any:
    """Custom JSON serializer for datetime objects."""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


def get_commons_domain(fm: Dict) -> List[str]:
    """
    Extract commons_domain from frontmatter.
    Supports both old format (root-level string) and new format (classification array).
    Always returns a list.
    """
    # New format: inside classification block
    classification = fm.get('classification', {})
    if isinstance(classification, dict):
        domain = classification.get('commons_domain')
        if domain:
            if isinstance(domain, list):
                return domain
            return [domain]
    
    # Old format: root-level
    domain = fm.get('commons_domain')
    if domain:
        if isinstance(domain, list):
            return domain
        return [domain]
    
    # Fallback
    return ['business']


def get_category(fm: Dict) -> List[str]:
    """
    Extract category from frontmatter.
    Always returns a list.
    """
    classification = fm.get('classification', {})
    if isinstance(classification, dict):
        cat = classification.get('category')
        if cat:
            if isinstance(cat, list):
                return cat
            return [cat]
    return []


def extract_relationships(frontmatter: Dict, entity_id: str) -> List[Dict]:
    """Extract relationships from frontmatter."""
    relationships = []
    
    # Direct relationship fields at root level
    rel_fields = ['generalizes_from', 'specializes_to', 'enables', 'requires', 'related']
    for rel_type in rel_fields:
        targets = frontmatter.get(rel_type, [])
        if isinstance(targets, list):
            for target in targets:
                if target and isinstance(target, str) and target.startswith('pat_'):
                    relationships.append({
                        'source': entity_id,
                        'target': target,
                        'type': rel_type
                    })
    
    # Legacy relationships dict
    rels = frontmatter.get('relationships', {})
    
    # Lighthouse relationships  
    if 'patterns_demonstrated' in frontmatter:
        rels['demonstrates'] = frontmatter.get('patterns_demonstrated', [])
    
    for rel_type, targets in rels.items():
        if isinstance(targets, list):
            for target in targets:
                if target and isinstance(target, str) and target.startswith('pat_'):
                    relationships.append({
                        'source': entity_id,
                        'target': target,
                        'type': rel_type
                    })
    
    return relationships


def extract_description(frontmatter: Dict, body: str) -> str:
    """Extract a description from frontmatter summary or body content.
    
    Prefers the 'summary' frontmatter field. Falls back to extracting
    the first meaningful paragraph from the body text, skipping
    markdown headers, tables, and horizontal rules.
    """
    # Prefer explicit summary
    summary = frontmatter.get('summary', '') or ''
    if summary.strip():
        return summary.strip()[:200]
    
    # Fall back to body content
    if not body:
        return ''
    
    lines = body.strip().split('\n')
    text_parts = []
    for line in lines:
        stripped = line.strip()
        # Skip empty lines, headers, tables, horizontal rules, and HTML
        if (not stripped or stripped.startswith('#') or stripped.startswith('|')
                or stripped.startswith('---') or stripped.startswith('<')):
            # If we already collected some text, stop at the next break
            if text_parts:
                break
            continue
        text_parts.append(stripped)
        if len(' '.join(text_parts)) >= 200:
            break
    
    return ' '.join(text_parts)[:200]


def build_search_index(patterns: List[Dict]) -> List[Dict]:
    """Build the search index for frontend search."""
    search_index = []
    
    for pattern in patterns:
        fm = pattern['frontmatter']
        body = pattern.get('body', '')
        domains = get_commons_domain(fm)
        categories = get_category(fm)
        
        search_item = {
            "title": fm.get('title', ''),
            "url": f"/patterns/{fm.get('slug', pattern['slug'])}/",
            "classification": categories,
            "description": extract_description(fm, body),
            "domains": domains,  # Array of domains
            "domain": domains[0] if domains else 'business',  # Primary domain for backward compatibility
            "score": fm.get('confidence_score', fm.get('classification', {}).get('commons_alignment', 3))
        }
        search_index.append(search_item)
    
    return search_index


def build_lite_index(patterns: List[Dict]) -> Dict:
    """Build the compact pattern index for ChatGPT GPT Actions.

    This file is consumed by the Commons Suit Lite GPT via its OpenAPI
    action schema. Format: {total, scores, patterns: [[title, filename, score], ...]}

    IMPORTANT: Do not remove or rename this file without updating the
    GPT's OpenAPI schema at the same time. External consumers depend on
    the exact path _data/pattern_index_lite.json.
    """
    score_counts: Dict[str, int] = {}
    pattern_list = []

    for pattern in patterns:
        fm = pattern['frontmatter']
        title = fm.get('title', '')
        filename = pattern['slug'] + '.md'
        # Use commons_alignment (integer 1-5) as the score.
        # Do NOT use confidence_score (float 0-1) — that's a different metric.
        score = fm.get('classification', {}).get('commons_alignment', 3)
        score = int(score) if score is not None else 3

        pattern_list.append([title, filename, score])

        score_key = str(score)
        score_counts[score_key] = score_counts.get(score_key, 0) + 1

    return {
        'total': len(pattern_list),
        'scores': score_counts,
        'patterns': sorted(pattern_list, key=lambda p: p[0])  # alphabetical
    }


def build_registry(patterns: List[Dict]) -> List[Dict]:
    """Build the registry mapping TypeIDs to patterns."""
    registry = []
    
    for pattern in patterns:
        fm = pattern['frontmatter']
        domains = get_commons_domain(fm)
        
        registry_item = {
            "id": fm.get('id', ''),
            "title": fm.get('title', ''),
            "slug": fm.get('slug', pattern['slug']),
            "domains": domains,  # Array of domains
            "domain": domains[0] if domains else 'business',  # Primary domain for backward compatibility
            "status": fm.get('status', fm.get('classification', {}).get('status', 'draft'))
        }
        registry.append(registry_item)
    
    return registry


def build_graph(patterns: List[Dict], lighthouses: List[Dict]) -> Dict:
    """Build the knowledge graph with nodes and edges."""
    graph = {
        'generated_at': datetime.utcnow().isoformat() + 'Z',
        'version': '3.0',  # Bumped for multi-domain support
        'nodes': {
            'patterns': [],
            'lighthouses': []
        },
        'edges': [],
        'stats': {
            'total_patterns': 0,
            'total_lighthouses': 0,
            'total_relationships': 0,
            'patterns_by_status': {},
            'patterns_by_domain': {},
            'multi_domain_patterns': 0
        }
    }
    
    # Process patterns
    for pattern in patterns:
        fm = pattern['frontmatter']
        domains = get_commons_domain(fm)
        categories = get_category(fm)
        classification = fm.get('classification', {})
        
        node = {
            'id': fm.get('id', ''),
            'title': fm.get('title', ''),
            'slug': fm.get('slug', pattern['slug']),
            'domains': domains,  # Array of domains
            'categories': categories,  # Array of categories
            'status': classification.get('status', fm.get('status', 'draft')),
            'commons_alignment': classification.get('commons_alignment'),
            'universality': classification.get('universality')
        }
        graph['nodes']['patterns'].append(node)
        
        # Extract relationships
        if fm.get('id'):
            rels = extract_relationships(fm, fm['id'])
            graph['edges'].extend(rels)
        
        # Update stats
        status = node['status']
        graph['stats']['patterns_by_status'][status] = graph['stats']['patterns_by_status'].get(status, 0) + 1
        
        # Count each domain the pattern belongs to
        for domain in domains:
            graph['stats']['patterns_by_domain'][domain] = graph['stats']['patterns_by_domain'].get(domain, 0) + 1
        
        # Count multi-domain patterns
        if len(domains) > 1:
            graph['stats']['multi_domain_patterns'] += 1
    
    # Process lighthouses
    for lighthouse in lighthouses:
        fm = lighthouse['frontmatter']
        
        node = {
            'id': fm.get('id', ''),
            'title': fm.get('title', ''),
            'slug': fm.get('slug', lighthouse['slug']),
            'type': fm.get('type', 'organization'),
            'status': fm.get('status', 'draft')
        }
        graph['nodes']['lighthouses'].append(node)
        
        # Extract relationships
        if fm.get('id'):
            rels = extract_relationships(fm, fm['id'])
            graph['edges'].extend(rels)
    
    # Final stats
    graph['stats']['total_patterns'] = len(graph['nodes']['patterns'])
    graph['stats']['total_lighthouses'] = len(graph['nodes']['lighthouses'])
    graph['stats']['total_relationships'] = len(graph['edges'])
    
    return graph


def load_entities(directory: Path) -> List[Dict]:
    """Load all entities from a directory."""
    entities = []
    
    if not directory.exists():
        return entities
    
    for filepath in sorted(directory.glob('*.md')):
        frontmatter, body = parse_frontmatter(filepath)
        if frontmatter:
            slug = filepath.stem
            entities.append({
                'filepath': filepath,
                'slug': slug,
                'frontmatter': frontmatter,
                'body': body
            })
    
    return entities


def main():
    print("=" * 60)
    print("COMMONS OS INDEX BUILDER v3.0")
    print("(Multi-domain support per ADR-012)")
    print("=" * 60)
    
    # Ensure output directories exist
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    # Load all entities
    print("\nLoading patterns...")
    patterns = load_entities(PATTERNS_DIR)
    print(f"  Found {len(patterns)} patterns")
    
    print("\nLoading lighthouses...")
    lighthouses = load_entities(LIGHTHOUSES_DIR)
    print(f"  Found {len(lighthouses)} lighthouses")
    
    # Build search index
    print("\nBuilding search index...")
    search_index = build_search_index(patterns)
    with open(SEARCH_INDEX_PATH, 'w', encoding='utf-8') as f:
        json.dump(search_index, f, indent=2, default=json_serializer)
    print(f"  Saved: {SEARCH_INDEX_PATH}")
    print(f"  Entries: {len(search_index)}")
    
    # Build registry
    print("\nBuilding registry...")
    registry = build_registry(patterns)
    with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, default=json_serializer)
    print(f"  Saved: {REGISTRY_PATH}")
    print(f"  Entries: {len(registry)}")
    
    # Build compact GPT Actions index
    print("\nBuilding GPT Actions lite index...")
    lite_index = build_lite_index(patterns)
    with open(LITE_INDEX_PATH, 'w', encoding='utf-8') as f:
        json.dump(lite_index, f, separators=(',', ':'))
    print(f"  Saved: {LITE_INDEX_PATH}")
    print(f"  Entries: {lite_index['total']}")
    print(f"  Size: {LITE_INDEX_PATH.stat().st_size:,} bytes")

    # Build knowledge graph
    print("\nBuilding knowledge graph...")
    graph = build_graph(patterns, lighthouses)
    graph_path = OUTPUT_DIR / "graph.json"
    with open(graph_path, 'w', encoding='utf-8') as f:
        json.dump(graph, f, indent=2, default=json_serializer)
    print(f"  Saved: {graph_path}")
    
    # Print summary
    print("\n" + "=" * 60)
    print("BUILD COMPLETE")
    print("=" * 60)
    print(f"Patterns:           {graph['stats']['total_patterns']}")
    print(f"Multi-domain:       {graph['stats']['multi_domain_patterns']}")
    print(f"Lighthouses:        {graph['stats']['total_lighthouses']}")
    print(f"Relationships:      {graph['stats']['total_relationships']}")
    print("\nDomain Distribution (patterns can appear in multiple):")
    for domain, count in sorted(graph['stats']['patterns_by_domain'].items(), key=lambda x: -x[1]):
        print(f"  {domain}: {count}")
    print("=" * 60)


if __name__ == "__main__":
    main()

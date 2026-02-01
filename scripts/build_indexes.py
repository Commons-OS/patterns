#!/usr/bin/env python3
"""
Build all indexes for the Commons OS Pattern Engine.

This single script generates all required index files from the source patterns:
- search-index.json: Frontend search functionality
- graph.json: Knowledge graph with relationships
- registry.json: TypeID to pattern mapping (used by Jekyll templates)

Run: python3 scripts/build_indexes.py
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


def extract_relationships(frontmatter: Dict, entity_id: str) -> List[Dict]:
    """Extract relationships from frontmatter."""
    relationships = []
    
    # Pattern relationships
    rels = frontmatter.get('relationships', {})
    
    # Lighthouse relationships  
    if 'patterns_demonstrated' in frontmatter:
        rels['demonstrates'] = frontmatter.get('patterns_demonstrated', [])
    
    for rel_type, targets in rels.items():
        if isinstance(targets, list):
            for target in targets:
                if target and isinstance(target, str):
                    relationships.append({
                        'source': entity_id,
                        'target': target,
                        'type': rel_type
                    })
    
    return relationships


def build_search_index(patterns: List[Dict]) -> List[Dict]:
    """Build the search index for frontend search."""
    search_index = []
    
    for pattern in patterns:
        fm = pattern['frontmatter']
        search_item = {
            "title": fm.get('title', ''),
            "url": f"/patterns/{fm.get('slug', pattern['slug'])}/",
            "classification": fm.get('classification', {}).get('keywords', []) if isinstance(fm.get('classification'), dict) else [],
            "description": (fm.get('summary', '') or '')[:200],
            "domain": fm.get('commons_domain', fm.get('domain', 'business')),
            "score": fm.get('confidence_score', 3)
        }
        search_index.append(search_item)
    
    return search_index


def build_registry(patterns: List[Dict]) -> List[Dict]:
    """Build the registry mapping TypeIDs to patterns."""
    registry = []
    
    for pattern in patterns:
        fm = pattern['frontmatter']
        registry_item = {
            "id": fm.get('id', ''),
            "title": fm.get('title', ''),
            "slug": fm.get('slug', pattern['slug']),
            "domain": fm.get('commons_domain', fm.get('domain', 'business')),
            "status": fm.get('status', 'draft')
        }
        registry.append(registry_item)
    
    return registry


def build_graph(patterns: List[Dict], lighthouses: List[Dict]) -> Dict:
    """Build the knowledge graph with nodes and edges."""
    graph = {
        'generated_at': datetime.utcnow().isoformat() + 'Z',
        'version': '2.0',
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
            'patterns_by_domain': {}
        }
    }
    
    # Process patterns
    for pattern in patterns:
        fm = pattern['frontmatter']
        
        node = {
            'id': fm.get('id', ''),
            'title': fm.get('title', ''),
            'slug': fm.get('slug', pattern['slug']),
            'domain': fm.get('commons_domain', fm.get('domain', 'business')),
            'status': fm.get('status', 'draft'),
            'confidence_score': fm.get('confidence_score'),
            'universality': fm.get('classification', {}).get('universality') if isinstance(fm.get('classification'), dict) else None
        }
        graph['nodes']['patterns'].append(node)
        
        # Extract relationships
        if fm.get('id'):
            rels = extract_relationships(fm, fm['id'])
            graph['edges'].extend(rels)
        
        # Update stats
        status = fm.get('status', 'draft')
        domain = fm.get('commons_domain', fm.get('domain', 'unknown'))
        graph['stats']['patterns_by_status'][status] = graph['stats']['patterns_by_status'].get(status, 0) + 1
        graph['stats']['patterns_by_domain'][domain] = graph['stats']['patterns_by_domain'].get(domain, 0) + 1
    
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
    print("COMMONS OS INDEX BUILDER")
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
    print(f"Patterns:      {graph['stats']['total_patterns']}")
    print(f"Lighthouses:   {graph['stats']['total_lighthouses']}")
    print(f"Relationships: {graph['stats']['total_relationships']}")
    print("\nDomains:")
    for domain, count in sorted(graph['stats']['patterns_by_domain'].items(), key=lambda x: -x[1]):
        print(f"  {domain}: {count}")
    print("=" * 60)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Knowledge Graph Builder for Commons OS Pattern Engine

Usage:
    python3 build_graph.py              # Build the full graph
    python3 build_graph.py --stats      # Show statistics only

This script traverses all canonical entities and builds a unified knowledge graph
stored in data/graph.json.
"""

import sys
import os
import json
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple


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


def extract_pattern_node(frontmatter: Dict, filepath: str) -> Dict:
    """Extract pattern node data from frontmatter."""
    tags = frontmatter.get('tags', {})
    
    return {
        'id': frontmatter.get('id', ''),
        'slug': frontmatter.get('slug', ''),
        'title': frontmatter.get('title', ''),
        'status': tags.get('status', 'draft'),
        'commons_alignment': tags.get('commons_alignment', 0),
        'domain': tags.get('domain', ''),
        'category': tags.get('category', []),
        'era': tags.get('era', []),
        'commons_domain': frontmatter.get('commons_domain', ''),
        'created': frontmatter.get('created', ''),
        'modified': frontmatter.get('modified', ''),
        'filepath': filepath
    }


def extract_lighthouse_node(frontmatter: Dict, filepath: str) -> Dict:
    """Extract lighthouse node data from frontmatter."""
    tags = frontmatter.get('tags', {})
    location = frontmatter.get('location', {})
    
    return {
        'id': frontmatter.get('id', ''),
        'slug': frontmatter.get('slug', ''),
        'title': frontmatter.get('title', ''),
        'status': tags.get('status', 'draft'),
        'commons_alignment': tags.get('commons_alignment', 0),
        'industry': tags.get('industry', []),
        'scale': tags.get('scale', ''),
        'region': tags.get('region', []),
        'location': location,
        'website': frontmatter.get('website', ''),
        'founded': frontmatter.get('founded', 0),
        'created': frontmatter.get('created', ''),
        'modified': frontmatter.get('modified', ''),
        'filepath': filepath
    }


def extract_relationships(frontmatter: Dict, entity_id: str) -> List[Dict]:
    """Extract relationships from frontmatter."""
    relationships = []
    
    # Pattern relationships
    pattern_rel_fields = {
        'generalizes_from': 'generalizes_from',
        'specializes_to': 'specializes_to',
        'enables': 'enables',
        'requires': 'requires',
        'related': 'related'
    }
    
    # Lighthouse relationships
    lighthouse_rel_fields = {
        'implements': 'implements',
        'inspired_by': 'inspired_by',
        'collaborates_with': 'collaborates_with',
        'related': 'related'
    }
    
    all_fields = {**pattern_rel_fields, **lighthouse_rel_fields}
    
    for field, rel_type in all_fields.items():
        if field in frontmatter and frontmatter[field]:
            for target_id in frontmatter[field]:
                if target_id:  # Skip empty strings
                    relationships.append({
                        'type': rel_type,
                        'source': entity_id,
                        'target': target_id,
                        'source_type': 'manual'
                    })
    
    return relationships


def build_graph(base_dir: Path) -> Dict:
    """Build the complete knowledge graph."""
    graph = {
        'version': '1.0',
        'generated': datetime.utcnow().isoformat() + 'Z',
        'stats': {
            'total_patterns': 0,
            'total_lighthouses': 0,
            'total_relationships': 0,
            'patterns_by_status': {},
            'lighthouses_by_status': {},
            'patterns_by_domain': {},
            'lighthouses_by_industry': {}
        },
        'nodes': {
            'patterns': [],
            'lighthouses': []
        },
        'edges': []
    }
    
    # Process patterns
    patterns_dir = base_dir / '_patterns'
    if patterns_dir.exists():
        for filepath in sorted(patterns_dir.glob('*.md')):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            frontmatter, _ = parse_frontmatter(content)
            if not frontmatter or 'id' not in frontmatter:
                continue
            
            node = extract_pattern_node(frontmatter, str(filepath.relative_to(base_dir)))
            graph['nodes']['patterns'].append(node)
            
            # Update stats
            graph['stats']['total_patterns'] += 1
            status = node.get('status', 'unknown')
            graph['stats']['patterns_by_status'][status] = graph['stats']['patterns_by_status'].get(status, 0) + 1
            
            domain = node.get('domain', 'unknown')
            graph['stats']['patterns_by_domain'][domain] = graph['stats']['patterns_by_domain'].get(domain, 0) + 1
            
            # Extract relationships
            rels = extract_relationships(frontmatter, frontmatter['id'])
            graph['edges'].extend(rels)
    
    # Process lighthouses
    lighthouses_dir = base_dir / '_lighthouses'
    if lighthouses_dir.exists():
        for filepath in sorted(lighthouses_dir.glob('*.md')):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            frontmatter, _ = parse_frontmatter(content)
            if not frontmatter or 'id' not in frontmatter:
                continue
            
            node = extract_lighthouse_node(frontmatter, str(filepath.relative_to(base_dir)))
            graph['nodes']['lighthouses'].append(node)
            
            # Update stats
            graph['stats']['total_lighthouses'] += 1
            status = node.get('status', 'unknown')
            graph['stats']['lighthouses_by_status'][status] = graph['stats']['lighthouses_by_status'].get(status, 0) + 1
            
            industries = node.get('industry', [])
            if isinstance(industries, list):
                for industry in industries:
                    graph['stats']['lighthouses_by_industry'][industry] = graph['stats']['lighthouses_by_industry'].get(industry, 0) + 1
            
            # Extract relationships
            rels = extract_relationships(frontmatter, frontmatter['id'])
            graph['edges'].extend(rels)
    
    graph['stats']['total_relationships'] = len(graph['edges'])
    
    return graph


def save_graph(graph: Dict, base_dir: Path):
    """Save the graph to disk."""
    output_path = base_dir / 'data' / 'graph.json'
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(graph, f, indent=2)
    
    print(f"Graph saved to: {output_path}")


def print_stats(graph: Dict):
    """Print graph statistics."""
    stats = graph['stats']
    
    print("\n" + "="*60)
    print("COMMONS OS KNOWLEDGE GRAPH STATISTICS")
    print("="*60)
    
    print(f"\n📊 TOTALS")
    print(f"   Patterns:      {stats['total_patterns']}")
    print(f"   Lighthouses:   {stats['total_lighthouses']}")
    print(f"   Relationships: {stats['total_relationships']}")
    
    print(f"\n📋 PATTERNS BY STATUS")
    for status, count in sorted(stats['patterns_by_status'].items()):
        print(f"   {status}: {count}")
    
    print(f"\n🏷️ PATTERNS BY DOMAIN")
    for domain, count in sorted(stats['patterns_by_domain'].items(), key=lambda x: -x[1]):
        print(f"   {domain}: {count}")
    
    if stats['total_lighthouses'] > 0:
        print(f"\n🏢 LIGHTHOUSES BY STATUS")
        for status, count in sorted(stats['lighthouses_by_status'].items()):
            print(f"   {status}: {count}")
        
        print(f"\n🏭 LIGHTHOUSES BY INDUSTRY")
        for industry, count in sorted(stats['lighthouses_by_industry'].items(), key=lambda x: -x[1]):
            print(f"   {industry}: {count}")
    
    print("\n" + "="*60)


def main():
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent
    
    print("Building knowledge graph...")
    graph = build_graph(base_dir)
    
    if '--stats' in sys.argv:
        print_stats(graph)
    else:
        save_graph(graph, base_dir)
        print_stats(graph)


if __name__ == '__main__':
    main()

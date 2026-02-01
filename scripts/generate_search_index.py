#!/usr/bin/env python3
"""
Generate search-index.json from pattern_index.json for the frontend search.
"""
import json
from pathlib import Path

def main():
    # Load the pattern index
    pattern_index_path = Path(__file__).parent.parent / "_data" / "pattern_index.json"
    search_index_path = Path(__file__).parent.parent / "search-index.json"
    
    with open(pattern_index_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Transform to search index format
    search_index = []
    for pattern in data.get('patterns', []):
        search_item = {
            "title": pattern.get('title', ''),
            "url": f"/patterns/{pattern.get('slug', '')}/",
            "tags": [],
            "description": pattern.get('description', '')[:200] if pattern.get('description') else '',
            "domain": pattern.get('domain', 'business'),
            "score": pattern.get('score', 3)
        }
        search_index.append(search_item)
    
    # Write the search index
    with open(search_index_path, 'w', encoding='utf-8') as f:
        json.dump(search_index, f, indent=2)
    
    print(f"Generated search index with {len(search_index)} patterns")
    print(f"Output: {search_index_path}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Generate a pattern index JSON file from all pattern markdown files.
This index is used by the Commons Suit GPT to discover and recommend patterns.
"""

import json
import os
import re
import yaml
from pathlib import Path
from datetime import datetime

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                return yaml.safe_load(parts[1]), parts[2]
            except yaml.YAMLError:
                return {}, content
    return {}, content

def extract_title(content, frontmatter):
    """Extract pattern title from frontmatter or first H1."""
    if 'title' in frontmatter:
        return frontmatter['title']
    
    # Look for first H1
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None

def extract_description(content):
    """Extract first paragraph as description."""
    # Skip frontmatter and find first substantial paragraph
    lines = content.strip().split('\n')
    paragraph = []
    in_paragraph = False
    
    for line in lines:
        line = line.strip()
        # Skip headers, empty lines at start
        if line.startswith('#') or line.startswith('---'):
            continue
        if not line and not in_paragraph:
            continue
        if not line and in_paragraph:
            break
        in_paragraph = True
        paragraph.append(line)
    
    description = ' '.join(paragraph)
    # Truncate to ~200 chars
    if len(description) > 200:
        description = description[:197] + '...'
    return description

def extract_score(content, frontmatter):
    """Extract Commons Alignment score from frontmatter or content."""
    # Check frontmatter first
    if 'commons_alignment' in frontmatter:
        return frontmatter['commons_alignment']
    
    # Look for score in Section 8
    match = re.search(r'\*\*Overall Score:\s*(\d)\s*\(', content)
    if match:
        return int(match.group(1))
    
    # Alternative format
    match = re.search(r'Score:\s*(\d)', content)
    if match:
        return int(match.group(1))
    
    return None

def extract_domain(frontmatter, filepath):
    """Extract domain from frontmatter or filepath."""
    if 'domain' in frontmatter:
        return frontmatter['domain']
    # Default to business for now
    return 'business'

def extract_universality(frontmatter):
    """Extract universality level from frontmatter."""
    if 'universality' in frontmatter:
        return frontmatter['universality']
    return None

def generate_slug(filepath):
    """Generate URL slug from filepath."""
    filename = os.path.basename(filepath)
    # Remove .md extension
    slug = filename.replace('.md', '')
    # Remove leading numbers and dashes (e.g., "1-" or "100-")
    slug = re.sub(r'^\d+-', '', slug)
    return slug

def process_pattern(filepath):
    """Process a single pattern file and extract metadata."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    frontmatter, body = extract_frontmatter(content)
    
    title = extract_title(body, frontmatter)
    if not title:
        title = generate_slug(filepath).replace('-', ' ').title()
    
    return {
        'slug': generate_slug(filepath),
        'title': title,
        'description': extract_description(body),
        'score': extract_score(content, frontmatter),
        'domain': extract_domain(frontmatter, filepath),
        'universality': extract_universality(frontmatter),
        'file': os.path.basename(filepath)
    }

def main():
    # Find patterns directory
    script_dir = Path(__file__).parent
    patterns_dir = script_dir.parent / '_patterns'
    
    if not patterns_dir.exists():
        print(f"Error: Patterns directory not found at {patterns_dir}")
        return
    
    # Process all pattern files
    patterns = []
    for filepath in sorted(patterns_dir.glob('*.md')):
        try:
            pattern = process_pattern(filepath)
            patterns.append(pattern)
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
    
    # Generate index
    index = {
        'generated_at': datetime.utcnow().isoformat() + 'Z',
        'total_patterns': len(patterns),
        'score_distribution': {},
        'patterns': patterns
    }
    
    # Calculate score distribution
    for pattern in patterns:
        score = pattern.get('score')
        if score:
            index['score_distribution'][str(score)] = index['score_distribution'].get(str(score), 0) + 1
    
    # Write index file
    output_path = script_dir.parent / '_data' / 'pattern_index.json'
    output_path.parent.mkdir(exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    print(f"Generated pattern index with {len(patterns)} patterns")
    print(f"Output: {output_path}")
    print(f"Score distribution: {index['score_distribution']}")

if __name__ == '__main__':
    main()

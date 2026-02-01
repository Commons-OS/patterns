#!/usr/bin/env python3
"""
Convert Existing Patterns to Staging Format

This script converts patterns from the old format (simple markdown with headers)
to the proper Pattern Engine format with:
- TypeID (UUID7-based)
- Full YAML frontmatter
- Proper content structure

Usage:
    python3 convert_to_staging.py <source_dir> <entity_type> [--dry-run]
    
Examples:
    python3 convert_to_staging.py /path/to/security_patterns pattern
    python3 convert_to_staging.py /path/to/startup_patterns pattern --dry-run
"""

import sys
import os
import re
import uuid
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple

# Add scripts directory to path for TypeID generation
sys.path.insert(0, str(Path(__file__).parent))
from generate_typeid import generate_typeid


def slugify(title: str) -> str:
    """Convert title to URL-friendly slug."""
    slug = title.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')


def extract_section(content: str, header: str) -> Optional[str]:
    """Extract content under a specific header."""
    pattern = rf'^##\s*{re.escape(header)}.*?\n(.*?)(?=^##|\Z)'
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None


def extract_7_pillars(content: str) -> Dict[str, float]:
    """Extract 7 Pillars scores from content."""
    pillars = {}
    pillar_names = ['Purpose', 'Governance', 'Culture', 'Incentives', 'Knowledge', 'Technology', 'Resilience']
    
    for pillar in pillar_names:
        # Look for patterns like "**Purpose**: 4.5" or "| Purpose | 4.5 |"
        pattern = rf'\*\*{pillar}\*\*[:\s]*(\d+\.?\d*)|{pillar}\s*\|\s*(\d+\.?\d*)'
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            score = match.group(1) or match.group(2)
            pillars[pillar.lower()] = float(score)
    
    return pillars


def extract_tags_from_content(content: str, title: str) -> Dict:
    """Infer tags from content analysis."""
    tags = {
        'universality': 'universal',
        'domain': [],
        'category': [],
        'era': 'modern',
        'origin': 'academic',
        'status': 'published',
        'commons_alignment': 'medium'
    }
    
    content_lower = content.lower()
    
    # Detect domain
    if any(term in content_lower for term in ['privacy', 'data protection', 'gdpr', 'consent']):
        tags['domain'].append('privacy')
    if any(term in content_lower for term in ['security', 'authentication', 'encryption', 'zero trust']):
        tags['domain'].append('security')
    if any(term in content_lower for term in ['sovereignty', 'data residency', 'self-sovereign', 'decentralized']):
        tags['domain'].append('sovereignty')
    if any(term in content_lower for term in ['artificial intelligence', 'machine learning', 'model', 'ai ']):
        tags['domain'].append('ai')
    if any(term in content_lower for term in ['startup', 'venture', 'founder', 'entrepreneur']):
        tags['domain'].append('startup')
    if any(term in content_lower for term in ['governance', 'organization', 'management']):
        tags['domain'].append('governance')
    
    if not tags['domain']:
        tags['domain'].append('general')
    
    # Detect era
    if any(term in content_lower for term in ['emerging', 'experimental', 'cutting-edge', 'novel']):
        tags['era'] = 'emerging'
    elif any(term in content_lower for term in ['traditional', 'classical', 'established']):
        tags['era'] = 'established'
    
    # Detect commons alignment from 7 pillars score if present
    pillars = extract_7_pillars(content)
    if pillars:
        avg_score = sum(pillars.values()) / len(pillars)
        if avg_score >= 4.5:
            tags['commons_alignment'] = 'very_high'
        elif avg_score >= 4.0:
            tags['commons_alignment'] = 'high'
        elif avg_score >= 3.0:
            tags['commons_alignment'] = 'medium'
        else:
            tags['commons_alignment'] = 'low'
    
    return tags


def parse_old_format(filepath: Path) -> Dict:
    """Parse a pattern in the old format (simple markdown)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title from first H1 or filename
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
    else:
        # Extract from filename like "P001-Data-Minimization.md"
        title = filepath.stem
        title = re.sub(r'^[A-Z]+\d+-', '', title)  # Remove prefix like P001-
        title = title.replace('-', ' ')
    
    # Extract sections
    overview = extract_section(content, 'Overview') or extract_section(content, 'Context')
    core_principles = extract_section(content, 'Core Principles')
    key_practices = extract_section(content, 'Key Practices')
    implementation = extract_section(content, 'Implementation')
    examples = extract_section(content, 'Examples') or extract_section(content, 'Case Studies')
    challenges = extract_section(content, 'Challenges')
    assessment = extract_section(content, '7 Pillars Assessment') or extract_section(content, 'Assessment')
    
    # Extract 7 pillars scores
    pillars = extract_7_pillars(content)
    
    # Infer tags
    tags = extract_tags_from_content(content, title)
    
    return {
        'title': title,
        'overview': overview,
        'core_principles': core_principles,
        'key_practices': key_practices,
        'implementation': implementation,
        'examples': examples,
        'challenges': challenges,
        'assessment': assessment,
        'pillars': pillars,
        'tags': tags,
        'original_content': content
    }


def generate_frontmatter(parsed: Dict, entity_type: str = 'pattern') -> str:
    """Generate YAML frontmatter for the pattern."""
    type_id = generate_typeid(entity_type)
    slug = slugify(parsed['title'])
    now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    tags = parsed['tags']
    pillars = parsed['pillars']
    
    # Calculate overall score
    overall_score = sum(pillars.values()) / len(pillars) if pillars else 3.5
    
    frontmatter = f"""---
id: {type_id}
slug: {slug}
title: "{parsed['title']}"
aliases: []
version: "1.0"
created: "{now}"
modified: "{now}"

tags:
  universality: {tags.get('universality', 'universal')}
  domain: {tags.get('domain', ['general'])}
  category: {tags.get('category', [])}
  era: {tags.get('era', 'modern')}
  origin: {tags.get('origin', 'academic')}
  status: draft
  commons_alignment: {tags.get('commons_alignment', 'medium')}

commons_domain: business
generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []

assessment:
  overall_score: {overall_score:.1f}
  pillars:
    purpose: {pillars.get('purpose', 3.5)}
    governance: {pillars.get('governance', 3.5)}
    culture: {pillars.get('culture', 3.5)}
    incentives: {pillars.get('incentives', 3.5)}
    knowledge: {pillars.get('knowledge', 3.5)}
    technology: {pillars.get('technology', 3.5)}
    resilience: {pillars.get('resilience', 3.5)}

contributors:
  - name: "Commons OS"
    role: "author"
    
sources: []
license: "CC-BY-SA-4.0"
attribution: "Commons OS Pattern Library"
repository: "https://github.com/Commons-OS/patterns"
---
"""
    return frontmatter


def generate_content(parsed: Dict) -> str:
    """Generate properly structured content body."""
    sections = []
    
    sections.append(f"# {parsed['title']}\n")
    
    if parsed.get('overview'):
        sections.append(f"## Overview\n\n{parsed['overview']}\n")
    
    if parsed.get('core_principles'):
        sections.append(f"## Core Principles\n\n{parsed['core_principles']}\n")
    
    if parsed.get('key_practices'):
        sections.append(f"## Key Practices\n\n{parsed['key_practices']}\n")
    
    if parsed.get('implementation'):
        sections.append(f"## Implementation\n\n{parsed['implementation']}\n")
    
    if parsed.get('examples'):
        sections.append(f"## Examples\n\n{parsed['examples']}\n")
    
    if parsed.get('challenges'):
        sections.append(f"## Challenges\n\n{parsed['challenges']}\n")
    
    if parsed.get('assessment'):
        sections.append(f"## 7 Pillars Assessment\n\n{parsed['assessment']}\n")
    
    return '\n'.join(sections)


def convert_pattern(source_path: Path, staging_dir: Path, entity_type: str = 'pattern', dry_run: bool = False) -> Optional[Path]:
    """Convert a single pattern to staging format."""
    print(f"Converting: {source_path.name}")
    
    try:
        parsed = parse_old_format(source_path)
        frontmatter = generate_frontmatter(parsed, entity_type)
        content = generate_content(parsed)
        
        full_content = frontmatter + "\n" + content
        
        # Generate output filename
        slug = slugify(parsed['title'])
        output_filename = f"{slug}.md"
        output_path = staging_dir / output_filename
        
        if dry_run:
            print(f"  Would create: {output_path}")
            print(f"  Title: {parsed['title']}")
            print(f"  Tags: {parsed['tags']['domain']}")
            return None
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        print(f"  Created: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"  ERROR: {e}")
        return None


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    
    source_dir = Path(sys.argv[1])
    entity_type = sys.argv[2]
    dry_run = '--dry-run' in sys.argv
    
    if not source_dir.exists():
        print(f"Error: Source directory not found: {source_dir}")
        sys.exit(1)
    
    if entity_type not in ['pattern', 'lighthouse']:
        print(f"Error: Entity type must be 'pattern' or 'lighthouse'")
        sys.exit(1)
    
    # Determine staging directory
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent
    staging_dir = base_dir / '_staging' / f"{entity_type}s"
    staging_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Source: {source_dir}")
    print(f"Staging: {staging_dir}")
    print(f"Entity type: {entity_type}")
    print(f"Dry run: {dry_run}")
    print("-" * 60)
    
    # Convert all markdown files
    converted = 0
    failed = 0
    
    for filepath in sorted(source_dir.glob('*.md')):
        if filepath.name.startswith('.'):
            continue
        result = convert_pattern(filepath, staging_dir, entity_type, dry_run)
        if result:
            converted += 1
        else:
            if not dry_run:
                failed += 1
    
    print("-" * 60)
    print(f"Converted: {converted}")
    if failed:
        print(f"Failed: {failed}")


if __name__ == '__main__':
    main()

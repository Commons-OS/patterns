#!/usr/bin/env python3
"""
Convert Existing Patterns to Staging Format

This script converts patterns from the old format (simple markdown with headers)
to the proper Pattern Engine format matching PATTERN_SPEC.md:
- TypeID (UUID7-based)
- Full YAML frontmatter with all required fields
- Proper numbered content structure

Usage:
    python3 convert_to_staging.py <source_dir> <entity_type> [--dry-run] [--start-number N]
    
Examples:
    python3 convert_to_staging.py /path/to/security_patterns pattern --start-number 1025
    python3 convert_to_staging.py /path/to/startup_patterns pattern --dry-run
"""

import sys
import os
import re
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


def detect_domain(content: str, title: str) -> str:
    """Detect the primary domain from content analysis."""
    content_lower = content.lower()
    title_lower = title.lower()
    
    # Check in order of specificity
    if any(term in content_lower for term in ['privacy', 'data protection', 'gdpr', 'consent', 'anonymization', 'pseudonymization']):
        return 'privacy'
    if any(term in content_lower for term in ['sovereignty', 'data residency', 'self-sovereign', 'decentralized identity', 'gaia-x']):
        return 'sovereignty'
    if any(term in content_lower for term in ['security', 'authentication', 'encryption', 'zero trust', 'vulnerability', 'firewall']):
        return 'security'
    if any(term in content_lower for term in ['artificial intelligence', 'machine learning', 'model training', 'inference', 'neural']):
        return 'technology'
    if any(term in content_lower for term in ['startup', 'venture', 'founder', 'entrepreneur', 'funding round']):
        return 'startup'
    if any(term in content_lower for term in ['governance', 'voting', 'decision-making', 'board', 'stakeholder']):
        return 'governance'
    if any(term in content_lower for term in ['culture', 'values', 'psychological safety', 'trust']):
        return 'culture'
    if any(term in content_lower for term in ['finance', 'capital', 'investment', 'revenue', 'pricing']):
        return 'finance'
    
    return 'operations'


def detect_commons_alignment(pillars: Dict[str, float]) -> int:
    """Calculate commons alignment score (1-5) from 7 pillars."""
    if not pillars:
        return 3  # Default to medium
    
    avg_score = sum(pillars.values()) / len(pillars)
    
    if avg_score >= 4.5:
        return 5
    elif avg_score >= 4.0:
        return 4
    elif avg_score >= 3.0:
        return 3
    elif avg_score >= 2.0:
        return 2
    else:
        return 1


def detect_era(content: str) -> str:
    """Detect the era from content analysis."""
    content_lower = content.lower()
    
    if any(term in content_lower for term in ['emerging', 'experimental', 'cutting-edge', 'novel', 'ai-powered']):
        return 'cognitive'
    elif any(term in content_lower for term in ['traditional', 'classical', 'established', 'industrial']):
        return 'industrial'
    
    return 'cognitive'  # Default to modern era


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
    overview = extract_section(content, 'Overview') or extract_section(content, 'Context') or ""
    core_principles = extract_section(content, 'Core Principles') or ""
    key_practices = extract_section(content, 'Key Practices') or ""
    implementation = extract_section(content, 'Implementation') or ""
    examples = extract_section(content, 'Examples') or extract_section(content, 'Case Studies') or ""
    challenges = extract_section(content, 'Challenges') or extract_section(content, 'Anti-Patterns') or ""
    assessment = extract_section(content, '7 Pillars Assessment') or extract_section(content, 'Assessment') or ""
    when_to_use = extract_section(content, 'When to Use') or ""
    references = extract_section(content, 'References') or ""
    
    # Extract 7 pillars scores
    pillars = extract_7_pillars(content)
    
    # Detect domain and alignment
    domain = detect_domain(content, title)
    commons_alignment = detect_commons_alignment(pillars)
    era = detect_era(content)
    
    return {
        'title': title,
        'overview': overview,
        'core_principles': core_principles,
        'key_practices': key_practices,
        'implementation': implementation,
        'examples': examples,
        'challenges': challenges,
        'assessment': assessment,
        'when_to_use': when_to_use,
        'references': references,
        'pillars': pillars,
        'domain': domain,
        'commons_alignment': commons_alignment,
        'era': era,
        'original_content': content
    }


def generate_frontmatter(parsed: Dict, entity_type: str, seq_number: int, filename: str) -> str:
    """Generate YAML frontmatter matching PATTERN_SPEC.md exactly."""
    type_id = generate_typeid(entity_type)
    slug = slugify(parsed['title'])
    full_slug = f"{seq_number}-{slug}"
    now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    pillars = parsed['pillars']
    
    # Calculate overall score
    overall_score = sum(pillars.values()) / len(pillars) if pillars else 3.5
    
    # Determine commons_domain based on primary domain
    domain = parsed['domain']
    if domain in ['security', 'privacy', 'sovereignty']:
        commons_domain = 'security'
    elif domain == 'startup':
        commons_domain = 'startup'
    else:
        commons_domain = 'business'
    
    frontmatter = f"""---
id: {type_id}
page_url: https://commons-os.github.io/patterns/{full_slug}/
github_url: https://github.com/commons-os/patterns/blob/main/_patterns/{filename}
slug: {full_slug}
title: "{parsed['title']}"
aliases: []
version: "1.0"
created: "{now}"
modified: "{now}"

tags:
  universality: universal
  domain: {domain}
  category: [practice]
  era: [{parsed['era']}]
  origin: [Commons OS]
  status: draft
  commons_alignment: {parsed['commons_alignment']}

commons_domain: {commons_domain}

generalizes_from: []
specializes_to: []
enables: []
requires: []
related: []

contributors: [commons-os]
sources: []
license: CC-BY-SA-4.0
attribution: Commons OS distributed by cloudsters, https://cloudsters.net
repository: https://github.com/commons-os/patterns
---
"""
    return frontmatter


def generate_content(parsed: Dict) -> str:
    """Generate properly structured content body with numbered sections."""
    sections = []
    
    # Section 1: Overview
    overview = parsed.get('overview', '')
    if not overview:
        overview = f"[Overview of {parsed['title']} pattern - to be completed]"
    sections.append(f"### 1. Overview\n\n{overview}\n")
    
    # Section 2: Core Principles
    core_principles = parsed.get('core_principles', '')
    if not core_principles:
        core_principles = "[Core principles - to be completed]"
    sections.append(f"### 2. Core Principles\n\n{core_principles}\n")
    
    # Section 3: Key Practices
    key_practices = parsed.get('key_practices', '')
    if not key_practices:
        key_practices = "[Key practices - to be completed]"
    sections.append(f"### 3. Key Practices\n\n{key_practices}\n")
    
    # Section 4: Implementation
    implementation = parsed.get('implementation', '')
    if not implementation:
        implementation = "[Implementation guidance - to be completed]"
    sections.append(f"### 4. Implementation\n\n{implementation}\n")
    
    # Section 5: 7 Pillars Assessment
    pillars = parsed.get('pillars', {})
    assessment_table = """| Pillar | Score (1-5) | Rationale |
|--------|-------------|-----------|
| Purpose | {purpose} | [Rationale] |
| Governance | {governance} | [Rationale] |
| Culture | {culture} | [Rationale] |
| Incentives | {incentives} | [Rationale] |
| Knowledge | {knowledge} | [Rationale] |
| Technology | {technology} | [Rationale] |
| Resilience | {resilience} | [Rationale] |
| **Overall** | **{overall:.1f}** | **[Summary]** |""".format(
        purpose=pillars.get('purpose', 3.5),
        governance=pillars.get('governance', 3.5),
        culture=pillars.get('culture', 3.5),
        incentives=pillars.get('incentives', 3.5),
        knowledge=pillars.get('knowledge', 3.5),
        technology=pillars.get('technology', 3.5),
        resilience=pillars.get('resilience', 3.5),
        overall=sum(pillars.values()) / len(pillars) if pillars else 3.5
    )
    sections.append(f"### 5. 7 Pillars Assessment\n\n{assessment_table}\n")
    
    # Section 6: When to Use
    when_to_use = parsed.get('when_to_use', '')
    if not when_to_use:
        when_to_use = "[When to use this pattern - to be completed]"
    sections.append(f"### 6. When to Use\n\n{when_to_use}\n")
    
    # Section 7: Anti-Patterns & Gotchas
    challenges = parsed.get('challenges', '')
    if not challenges:
        challenges = "[Anti-patterns and gotchas - to be completed]"
    sections.append(f"### 7. Anti-Patterns & Gotchas\n\n{challenges}\n")
    
    # Section 8: References
    references = parsed.get('references', '')
    if not references:
        references = "[References - to be completed]"
    sections.append(f"### 8. References\n\n{references}\n")
    
    return '\n'.join(sections)


def convert_pattern(source_path: Path, staging_dir: Path, entity_type: str, seq_number: int, dry_run: bool = False) -> Optional[Path]:
    """Convert a single pattern to staging format."""
    print(f"Converting: {source_path.name}")
    
    try:
        parsed = parse_old_format(source_path)
        
        # Generate filename
        slug = slugify(parsed['title'])
        filename = f"{seq_number}-{slug}.md"
        
        frontmatter = generate_frontmatter(parsed, entity_type, seq_number, filename)
        content = generate_content(parsed)
        
        full_content = frontmatter + "\n" + content
        
        output_path = staging_dir / filename
        
        if dry_run:
            print(f"  Would create: {output_path}")
            print(f"  Title: {parsed['title']}")
            print(f"  Domain: {parsed['domain']}")
            print(f"  Commons Alignment: {parsed['commons_alignment']}")
            return None
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        print(f"  Created: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"  ERROR: {e}")
        import traceback
        traceback.print_exc()
        return None


def get_next_sequential_number(patterns_dir: Path) -> int:
    """Get the next available sequential number from existing patterns."""
    max_num = 0
    for filepath in patterns_dir.glob('*.md'):
        match = re.match(r'^(\d+)-', filepath.name)
        if match:
            num = int(match.group(1))
            max_num = max(max_num, num)
    return max_num + 1


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    
    source_dir = Path(sys.argv[1])
    entity_type = sys.argv[2]
    dry_run = '--dry-run' in sys.argv
    
    # Check for start number override
    start_number = None
    for i, arg in enumerate(sys.argv):
        if arg == '--start-number' and i + 1 < len(sys.argv):
            start_number = int(sys.argv[i + 1])
    
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
    
    # Determine starting sequential number
    if start_number is None:
        # Check existing patterns in _patterns/
        patterns_dir = base_dir / '_patterns'
        start_number = get_next_sequential_number(patterns_dir)
    
    print(f"Source: {source_dir}")
    print(f"Staging: {staging_dir}")
    print(f"Entity type: {entity_type}")
    print(f"Starting number: {start_number}")
    print(f"Dry run: {dry_run}")
    print("-" * 60)
    
    # Convert all markdown files
    converted = 0
    failed = 0
    current_number = start_number
    
    for filepath in sorted(source_dir.glob('*.md')):
        if filepath.name.startswith('.'):
            continue
        result = convert_pattern(filepath, staging_dir, entity_type, current_number, dry_run)
        if result:
            converted += 1
            current_number += 1
        else:
            if not dry_run:
                failed += 1
            else:
                current_number += 1  # Still increment in dry run
    
    print("-" * 60)
    print(f"Converted: {converted}")
    print(f"Number range: {start_number} - {current_number - 1}")
    if failed:
        print(f"Failed: {failed}")


if __name__ == '__main__':
    main()

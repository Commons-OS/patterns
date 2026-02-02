#!/usr/bin/env python3
"""
Migration script to convert commons_domain from single string to array
and move it inside the classification block.

Per ADR-012: Multi-Value Classification Fields
"""

import os
import re
import yaml
from pathlib import Path

# Patterns directory
PATTERNS_DIR = Path("_patterns")

# Keywords that indicate a pattern should have BOTH business AND startup domains
STARTUP_KEYWORDS = [
    'lean', 'mvp', 'minimum viable', 'startup', 'founder', 'venture', 
    'pivot', 'validation', 'customer discovery', 'product-market',
    'bootstrap', 'seed', 'series a', 'angel', 'accelerator', 'incubator',
    'canvas', 'ries', 'blank', 'y combinator', 'yc', 'growth hack',
    'early adopter', 'beachhead', 'traction', 'runway', 'burn rate',
    'cap table', 'term sheet', 'due diligence', 'pitch deck',
    'value proposition', 'customer segment', 'jobs to be done', 'jtbd',
    'freemium', 'product-led', 'viral', 'network effect'
]

# Keywords that indicate security domain
SECURITY_KEYWORDS = [
    'security', 'privacy', 'encryption', 'authentication', 'authorization',
    'zero trust', 'defense in depth', 'threat', 'vulnerability', 'attack',
    'penetration', 'firewall', 'intrusion', 'malware', 'ransomware',
    'data protection', 'gdpr', 'compliance', 'audit', 'access control',
    'identity', 'credential', 'certificate', 'ssl', 'tls', 'vpn',
    'sovereignty', 'self-sovereign', 'decentralized identity'
]

def should_add_startup_domain(content: str, title: str) -> bool:
    """Check if pattern should also have startup domain."""
    text = (content + " " + title).lower()
    return any(kw in text for kw in STARTUP_KEYWORDS)

def should_add_security_domain(content: str, title: str) -> bool:
    """Check if pattern should also have security domain."""
    text = (content + " " + title).lower()
    return any(kw in text for kw in SECURITY_KEYWORDS)

def should_add_business_domain(content: str, title: str) -> bool:
    """Check if startup/security pattern should also have business domain."""
    # Most startup and security patterns are also relevant to business
    # Exception: very specific technical security patterns
    text = (content + " " + title).lower()
    technical_only = ['cve', 'exploit', 'buffer overflow', 'sql injection', 
                      'xss', 'csrf', 'penetration test']
    return not any(kw in text for kw in technical_only)

def migrate_pattern(filepath: Path) -> dict:
    """Migrate a single pattern file to multi-domain format."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split frontmatter and body
    parts = content.split('---', 2)
    if len(parts) < 3:
        return {'file': str(filepath), 'status': 'error', 'reason': 'Invalid frontmatter'}
    
    try:
        frontmatter = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        return {'file': str(filepath), 'status': 'error', 'reason': f'YAML error: {e}'}
    
    body = parts[2]
    title = frontmatter.get('title', '')
    
    # Get current commons_domain (could be at root or in classification)
    current_domain = frontmatter.get('commons_domain')
    if current_domain is None and 'classification' in frontmatter:
        current_domain = frontmatter.get('classification', {}).get('commons_domain')
    
    if current_domain is None:
        current_domain = 'business'  # Default
    
    # Convert to list if string
    if isinstance(current_domain, str):
        domains = [current_domain]
    else:
        domains = list(current_domain)
    
    # Add additional domains based on content
    if 'business' in domains:
        if should_add_startup_domain(body, title) and 'startup' not in domains:
            domains.append('startup')
        if should_add_security_domain(body, title) and 'security' not in domains:
            domains.append('security')
    
    if 'startup' in domains:
        if should_add_business_domain(body, title) and 'business' not in domains:
            domains.append('business')
    
    if 'security' in domains:
        if should_add_business_domain(body, title) and 'business' not in domains:
            domains.append('business')
    
    # Remove root-level commons_domain if present
    if 'commons_domain' in frontmatter:
        del frontmatter['commons_domain']
    
    # Ensure classification exists
    if 'classification' not in frontmatter:
        frontmatter['classification'] = {}
    
    # Set commons_domain as array inside classification
    frontmatter['classification']['commons_domain'] = domains
    
    # Ensure category is also an array
    if 'category' in frontmatter.get('classification', {}):
        cat = frontmatter['classification']['category']
        if isinstance(cat, str):
            frontmatter['classification']['category'] = [cat]
    
    # Rebuild the file
    new_content = '---\n' + yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False) + '---' + body
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return {
        'file': str(filepath),
        'status': 'migrated',
        'domains': domains,
        'added': [d for d in domains if d != current_domain] if isinstance(current_domain, str) else []
    }

def main():
    """Run migration on all patterns."""
    results = {
        'migrated': 0,
        'errors': 0,
        'multi_domain': 0,
        'details': []
    }
    
    pattern_files = list(PATTERNS_DIR.glob('*.md'))
    print(f"Found {len(pattern_files)} patterns to migrate")
    
    for filepath in pattern_files:
        result = migrate_pattern(filepath)
        results['details'].append(result)
        
        if result['status'] == 'migrated':
            results['migrated'] += 1
            if len(result['domains']) > 1:
                results['multi_domain'] += 1
        else:
            results['errors'] += 1
    
    print(f"\n=== Migration Complete ===")
    print(f"Migrated: {results['migrated']}")
    print(f"Errors: {results['errors']}")
    print(f"Multi-domain patterns: {results['multi_domain']}")
    
    # Show some examples of multi-domain patterns
    multi = [r for r in results['details'] if r['status'] == 'migrated' and len(r.get('domains', [])) > 1]
    print(f"\nExamples of multi-domain patterns:")
    for r in multi[:10]:
        print(f"  {r['file']}: {r['domains']}")
    
    # Show errors
    errors = [r for r in results['details'] if r['status'] == 'error']
    if errors:
        print(f"\nErrors:")
        for r in errors:
            print(f"  {r['file']}: {r['reason']}")

if __name__ == '__main__':
    main()

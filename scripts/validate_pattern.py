#!/usr/bin/env python3
"""
Pattern Validation Script for Commons OS Pattern Engine

Usage:
    python3 validate_pattern.py <pattern_file.md>
    python3 validate_pattern.py --all  # Validate all patterns in _patterns/

This script validates that a pattern file conforms to the PATTERN_SPEC.md specification.
"""

import sys
import os
import re
import yaml
from pathlib import Path
from datetime import datetime

# Required YAML fields
REQUIRED_FIELDS = [
    'id', 'page_url', 'github_url', 'slug', 'title', 'aliases', 'version',
    'created', 'modified', 'classification', 'commons_domain', 'generalizes_from',
    'specializes_to', 'enables', 'requires', 'related', 'contributors',
    'sources', 'license', 'attribution', 'repository'
]

REQUIRED_TAG_FIELDS = [
    'universality', 'domain', 'category', 'era', 'origin', 'status', 'commons_alignment'
]

VALID_UNIVERSALITY = ['universal', 'domain', 'implementation', 'context-specific', 'human-universal', 'design', 'meta', 'culture']
VALID_DOMAINS = ['governance', 'operations', 'finance', 'technology', 'culture', 
                 'security', 'privacy', 'sovereignty', 'startup']
VALID_CATEGORIES = ['framework', 'practice', 'principle', 'tool', 'structure', 'process', 'anti-pattern']
VALID_ERAS = ['pre-industrial', 'industrial', 'cognitive']
VALID_STATUS = ['draft', 'review', 'published']
VALID_COMMONS_DOMAINS = ['business', 'security', 'startup', 'urban', 'ecology', 'life']

# TypeID pattern: pat_ followed by 26 alphanumeric characters
TYPEID_PATTERN = re.compile(r'^pat_[a-z0-9]{20,30}$')

# Filename pattern: slug.md (lowercase, hyphens, alphanumeric)
FILENAME_PATTERN = re.compile(r'^[a-z0-9][a-z0-9-]*\.md$')


class ValidationError:
    def __init__(self, message, severity='error'):
        self.message = message
        self.severity = severity  # 'error' or 'warning'
    
    def __str__(self):
        return f"[{self.severity.upper()}] {self.message}"


def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return None, "File does not start with YAML frontmatter (---)"
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, "Invalid YAML frontmatter format"
    
    try:
        frontmatter = yaml.safe_load(parts[1])
        return frontmatter, None
    except yaml.YAMLError as e:
        return None, f"YAML parsing error: {e}"


def validate_typeid(id_value):
    """Validate that ID is in TypeID format."""
    if not TYPEID_PATTERN.match(id_value):
        return ValidationError(f"ID '{id_value}' is not in TypeID format (pat_{{uuid7}})")
    return None


def validate_filename(filepath):
    """Validate filename format."""
    filename = os.path.basename(filepath)
    if not FILENAME_PATTERN.match(filename):
        return ValidationError(f"Filename '{filename}' does not match format '{{slug}}.md' (lowercase, hyphens, alphanumeric)")
    return None


def validate_slug_matches_filename(slug, filepath):
    """Validate that slug matches filename."""
    filename = os.path.basename(filepath).replace('.md', '')
    if slug != filename:
        return ValidationError(f"Slug '{slug}' does not match filename '{filename}'")
    return None


def validate_required_fields(frontmatter):
    """Check that all required fields are present."""
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in frontmatter:
            errors.append(ValidationError(f"Missing required field: {field}"))
    
    # Check nested tag fields
    if 'classification' in frontmatter and isinstance(frontmatter['classification'], dict):
        for tag_field in REQUIRED_TAG_FIELDS:
            if tag_field not in frontmatter['classification']:
                errors.append(ValidationError(f"Missing required tag field: classification.{tag_field}"))
    
    return errors


def validate_field_values(frontmatter):
    """Validate that field values are correct."""
    errors = []
    
    # Validate tags
    if 'classification' in frontmatter and isinstance(frontmatter['classification'], dict):
        classification = frontmatter['classification']
        
        if 'universality' in classification and classification['universality'] not in VALID_UNIVERSALITY:
            errors.append(ValidationError(f"Invalid universality: {classification['universality']}. Must be one of {VALID_UNIVERSALITY}"))
        
        if 'domain' in classification and classification['domain'] not in VALID_DOMAINS:
            errors.append(ValidationError(f"Invalid domain: {classification['domain']}. Must be one of {VALID_DOMAINS}"))
        
        if 'status' in classification and classification['status'] not in VALID_STATUS:
            errors.append(ValidationError(f"Invalid status: {classification['status']}. Must be one of {VALID_STATUS}"))
        
        if 'commons_alignment' in classification:
            alignment = classification['commons_alignment']
            if not isinstance(alignment, (int, float)) or alignment < 1 or alignment > 5:
                errors.append(ValidationError(f"Invalid commons_alignment: {alignment}. Must be between 1 and 5"))
    
    # Validate commons_domain
    if 'commons_domain' in frontmatter and frontmatter['commons_domain'] not in VALID_COMMONS_DOMAINS:
        errors.append(ValidationError(f"Invalid commons_domain: {frontmatter['commons_domain']}. Must be one of {VALID_COMMONS_DOMAINS}"))
    
    return errors


def validate_relationships(frontmatter, all_ids=None):
    """Validate that relationship references are valid TypeIDs."""
    errors = []
    relationship_fields = ['generalizes_from', 'specializes_to', 'enables', 'requires', 'related']
    
    for field in relationship_fields:
        if field in frontmatter and frontmatter[field]:
            for ref in frontmatter[field]:
                if not TYPEID_PATTERN.match(ref):
                    errors.append(ValidationError(f"Invalid TypeID in {field}: {ref}"))
                elif all_ids and ref not in all_ids:
                    errors.append(ValidationError(f"Referenced pattern not found in {field}: {ref}", severity='warning'))
    
    return errors


def validate_content_structure(content):
    """Validate that content follows the required structure."""
    errors = []
    required_sections = [
        '### 1. Overview',
        '### 2. Core Principles',
        '### 3. Key Practices',
        '### 4. Implementation',
        '### 5. 7 Pillars Assessment',
        '### 6. When to Use',
        '### 7. Anti-Patterns',
        '### 8. References'
    ]
    
    for section in required_sections:
        # Allow for slight variations in section naming
        section_base = section.split('.')[0] + '.'
        if section_base not in content and section not in content:
            errors.append(ValidationError(f"Missing section: {section}", severity='warning'))
    
    return errors


def validate_pattern(filepath, all_ids=None):
    """Validate a single pattern file."""
    errors = []
    
    # Check file exists
    if not os.path.exists(filepath):
        return [ValidationError(f"File not found: {filepath}")]
    
    # Check filename format
    filename_error = validate_filename(filepath)
    if filename_error:
        errors.append(filename_error)
    
    # Read file content
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse frontmatter
    frontmatter, parse_error = parse_frontmatter(content)
    if parse_error:
        errors.append(ValidationError(parse_error))
        return errors
    
    # Validate required fields
    errors.extend(validate_required_fields(frontmatter))
    
    # Validate TypeID
    if 'id' in frontmatter:
        id_error = validate_typeid(frontmatter['id'])
        if id_error:
            errors.append(id_error)
    
    # Validate slug matches filename
    if 'slug' in frontmatter:
        slug_error = validate_slug_matches_filename(frontmatter['slug'], filepath)
        if slug_error:
            errors.append(slug_error)
    
    # Validate field values
    errors.extend(validate_field_values(frontmatter))
    
    # Validate relationships
    errors.extend(validate_relationships(frontmatter, all_ids))
    
    # Validate content structure
    errors.extend(validate_content_structure(content))
    
    return errors


def get_all_pattern_ids(patterns_dir):
    """Get all pattern IDs from the patterns directory."""
    ids = set()
    for filepath in Path(patterns_dir).glob('*.md'):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        frontmatter, _ = parse_frontmatter(content)
        if frontmatter and 'id' in frontmatter:
            ids.add(frontmatter['id'])
    return ids


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate_pattern.py <pattern_file.md>")
        print("       python3 validate_pattern.py --all")
        sys.exit(1)
    
    # Determine patterns directory
    script_dir = Path(__file__).parent
    patterns_dir = script_dir.parent / '_patterns'
    
    if sys.argv[1] == '--all':
        # Validate all patterns
        all_ids = get_all_pattern_ids(patterns_dir)
        total_errors = 0
        total_warnings = 0
        
        for filepath in sorted(patterns_dir.glob('*.md')):
            errors = validate_pattern(str(filepath), all_ids)
            if errors:
                print(f"\n{filepath.name}:")
                for error in errors:
                    print(f"  {error}")
                    if error.severity == 'error':
                        total_errors += 1
                    else:
                        total_warnings += 1
        
        print(f"\n{'='*50}")
        print(f"Total: {total_errors} errors, {total_warnings} warnings")
        sys.exit(1 if total_errors > 0 else 0)
    else:
        # Validate single file
        filepath = sys.argv[1]
        all_ids = get_all_pattern_ids(patterns_dir) if patterns_dir.exists() else None
        errors = validate_pattern(filepath, all_ids)
        
        if errors:
            print(f"Validation errors for {filepath}:")
            for error in errors:
                print(f"  {error}")
            sys.exit(1)
        else:
            print(f"✓ {filepath} is valid")
            sys.exit(0)


if __name__ == '__main__':
    main()

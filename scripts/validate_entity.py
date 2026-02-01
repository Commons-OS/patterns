#!/usr/bin/env python3
"""
Entity Validation Script for Commons OS Pattern Engine

Usage:
    python3 validate_entity.py <entity_file.md>
    python3 validate_entity.py --all              # Validate all entities
    python3 validate_entity.py --staging          # Validate only staging entities

This script validates that pattern and lighthouse files conform to their specifications.
"""

import sys
import os
import re
import yaml
from pathlib import Path
from datetime import datetime

# TypeID patterns
TYPEID_PATTERN = re.compile(r'^pat_[a-z0-9]{20,30}$')
TYPEID_LIGHTHOUSE = re.compile(r'^lh_[a-z0-9]{20,30}$')
TYPEID_ANY = re.compile(r'^(pat|lh)_[a-z0-9]{20,30}$')

# Filename pattern: number-slug.md
FILENAME_PATTERN = re.compile(r'^(\d+)-([a-z0-9-]+)\.md$')

# Valid values
VALID_STATUS = ['draft', 'review', 'published', 'mature', 'deprecated']
VALID_PATTERN_DOMAINS = ['governance', 'operations', 'finance', 'technology', 'culture', 
                         'security', 'privacy', 'sovereignty', 'startup']
VALID_COMMONS_DOMAINS = ['business', 'security', 'startup', 'urban', 'ecology', 'life']
VALID_LIGHTHOUSE_INDUSTRIES = ['technology', 'agriculture', 'finance', 'healthcare', 
                                'education', 'manufacturing', 'retail', 'services', 
                                'nonprofit', 'government']
VALID_SCALES = ['startup', 'small', 'medium', 'large', 'global']
VALID_REGIONS = ['north-america', 'south-america', 'europe', 'asia', 'africa', 'oceania', 'global']

# Required fields
REQUIRED_PATTERN_FIELDS = [
    'id', 'page_url', 'github_url', 'slug', 'title', 'aliases', 'version',
    'created', 'modified', 'tags', 'commons_domain', 'generalizes_from',
    'specializes_to', 'enables', 'requires', 'related', 'contributors',
    'sources', 'license', 'attribution', 'repository'
]

REQUIRED_PATTERN_TAG_FIELDS = [
    'universality', 'domain', 'category', 'era', 'origin', 'status', 'commons_alignment'
]

REQUIRED_LIGHTHOUSE_FIELDS = [
    'id', 'page_url', 'github_url', 'slug', 'title', 'aliases', 'version',
    'created', 'modified', 'tags', 'location', 'implements', 'inspired_by',
    'collaborates_with', 'related', 'website', 'founded', 'contributors',
    'sources', 'license', 'attribution', 'repository'
]

REQUIRED_LIGHTHOUSE_TAG_FIELDS = [
    'industry', 'scale', 'region', 'era', 'status', 'commons_alignment'
]


class ValidationError:
    def __init__(self, message, severity='error'):
        self.message = message
        self.severity = severity
    
    def __str__(self):
        icon = '❌' if self.severity == 'error' else '⚠️'
        return f"{icon} [{self.severity.upper()}] {self.message}"


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


def detect_entity_type(filepath, frontmatter=None):
    """Detect whether this is a pattern or lighthouse."""
    if frontmatter and 'id' in frontmatter:
        if frontmatter['id'].startswith('pat_'):
            return 'pattern'
        elif frontmatter['id'].startswith('lh_'):
            return 'lighthouse'
    
    # Fallback to path-based detection
    if '_lighthouses' in str(filepath) or 'lighthouses' in str(filepath):
        return 'lighthouse'
    return 'pattern'


def validate_typeid(id_value, entity_type):
    """Validate that ID is in correct TypeID format."""
    if entity_type == 'pattern':
        if not TYPEID_PATTERN.match(id_value):
            return ValidationError(f"ID '{id_value}' is not in pattern TypeID format (pat_{{uuid7}})")
    else:
        if not TYPEID_LIGHTHOUSE.match(id_value):
            return ValidationError(f"ID '{id_value}' is not in lighthouse TypeID format (lh_{{uuid7}})")
    return None


def validate_filename(filepath):
    """Validate filename format."""
    filename = os.path.basename(filepath)
    if not FILENAME_PATTERN.match(filename):
        return ValidationError(f"Filename '{filename}' does not match format '{{number}}-{{slug}}.md'")
    return None


def validate_slug_matches_filename(slug, filepath):
    """Validate that slug matches filename."""
    filename = os.path.basename(filepath).replace('.md', '')
    if slug != filename:
        return ValidationError(f"Slug '{slug}' does not match filename '{filename}'")
    return None


def validate_required_fields(frontmatter, entity_type):
    """Check that all required fields are present."""
    errors = []
    
    required_fields = REQUIRED_PATTERN_FIELDS if entity_type == 'pattern' else REQUIRED_LIGHTHOUSE_FIELDS
    required_tag_fields = REQUIRED_PATTERN_TAG_FIELDS if entity_type == 'pattern' else REQUIRED_LIGHTHOUSE_TAG_FIELDS
    
    for field in required_fields:
        if field not in frontmatter:
            errors.append(ValidationError(f"Missing required field: {field}"))
    
    if 'tags' in frontmatter and isinstance(frontmatter['tags'], dict):
        for tag_field in required_tag_fields:
            if tag_field not in frontmatter['tags']:
                errors.append(ValidationError(f"Missing required tag field: tags.{tag_field}"))
    
    return errors


def validate_field_values(frontmatter, entity_type):
    """Validate that field values are correct."""
    errors = []
    
    if 'tags' in frontmatter and isinstance(frontmatter['tags'], dict):
        tags = frontmatter['tags']
        
        if 'status' in tags and tags['status'] not in VALID_STATUS:
            errors.append(ValidationError(f"Invalid status: {tags['status']}. Must be one of {VALID_STATUS}"))
        
        if 'commons_alignment' in tags:
            alignment = tags['commons_alignment']
            if not isinstance(alignment, (int, float)) or alignment < 1 or alignment > 5:
                errors.append(ValidationError(f"Invalid commons_alignment: {alignment}. Must be between 1 and 5"))
        
        if entity_type == 'pattern':
            if 'domain' in tags and tags['domain'] not in VALID_PATTERN_DOMAINS:
                errors.append(ValidationError(f"Invalid domain: {tags['domain']}. Must be one of {VALID_PATTERN_DOMAINS}"))
        
        if entity_type == 'lighthouse':
            if 'scale' in tags and tags['scale'] not in VALID_SCALES:
                errors.append(ValidationError(f"Invalid scale: {tags['scale']}. Must be one of {VALID_SCALES}"))
    
    if entity_type == 'pattern':
        if 'commons_domain' in frontmatter and frontmatter['commons_domain'] not in VALID_COMMONS_DOMAINS:
            errors.append(ValidationError(f"Invalid commons_domain: {frontmatter['commons_domain']}"))
    
    return errors


def validate_relationships(frontmatter, entity_type, all_ids=None):
    """Validate that relationship references are valid TypeIDs."""
    errors = []
    
    if entity_type == 'pattern':
        relationship_fields = ['generalizes_from', 'specializes_to', 'enables', 'requires', 'related']
    else:
        relationship_fields = ['implements', 'inspired_by', 'collaborates_with', 'related']
    
    for field in relationship_fields:
        if field in frontmatter and frontmatter[field]:
            for ref in frontmatter[field]:
                if not TYPEID_ANY.match(ref):
                    errors.append(ValidationError(f"Invalid TypeID in {field}: {ref}"))
                elif all_ids and ref not in all_ids:
                    errors.append(ValidationError(f"Referenced entity not found in {field}: {ref}", severity='warning'))
    
    return errors


def validate_content_structure(content, entity_type):
    """Validate that content follows the required structure."""
    errors = []
    
    if entity_type == 'pattern':
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
    else:
        required_sections = [
            '### 1. Overview',
            '### 2. Patterns in Action',
            '### 3. Key Innovations',
            '### 4. Impact',
            '### 5. 7 Pillars Assessment',
            '### 6. Lessons Learned',
            '### 7. Challenges',
            '### 8. References'
        ]
    
    for section in required_sections:
        section_num = section.split('.')[0] + '.'
        if section_num not in content and section not in content:
            errors.append(ValidationError(f"Missing section: {section}", severity='warning'))
    
    return errors


def validate_entity(filepath, all_ids=None):
    """Validate a single entity file."""
    errors = []
    
    if not os.path.exists(filepath):
        return [ValidationError(f"File not found: {filepath}")]
    
    filename_error = validate_filename(filepath)
    if filename_error:
        errors.append(filename_error)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    frontmatter, parse_error = parse_frontmatter(content)
    if parse_error:
        errors.append(ValidationError(parse_error))
        return errors
    
    entity_type = detect_entity_type(filepath, frontmatter)
    
    errors.extend(validate_required_fields(frontmatter, entity_type))
    
    if 'id' in frontmatter:
        id_error = validate_typeid(frontmatter['id'], entity_type)
        if id_error:
            errors.append(id_error)
    
    if 'slug' in frontmatter:
        slug_error = validate_slug_matches_filename(frontmatter['slug'], filepath)
        if slug_error:
            errors.append(slug_error)
    
    errors.extend(validate_field_values(frontmatter, entity_type))
    errors.extend(validate_relationships(frontmatter, entity_type, all_ids))
    errors.extend(validate_content_structure(content, entity_type))
    
    return errors


def get_all_entity_ids(base_dir):
    """Get all entity IDs from the repository."""
    ids = set()
    
    for subdir in ['_patterns', '_lighthouses', '_staging/patterns', '_staging/lighthouses']:
        dir_path = Path(base_dir) / subdir
        if dir_path.exists():
            for filepath in dir_path.glob('*.md'):
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                frontmatter, _ = parse_frontmatter(content)
                if frontmatter and 'id' in frontmatter:
                    ids.add(frontmatter['id'])
    
    return ids


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate_entity.py <entity_file.md>")
        print("       python3 validate_entity.py --all")
        print("       python3 validate_entity.py --staging")
        sys.exit(1)
    
    script_dir = Path(__file__).parent
    base_dir = script_dir.parent
    
    if sys.argv[1] == '--all':
        dirs_to_check = ['_patterns', '_lighthouses']
    elif sys.argv[1] == '--staging':
        dirs_to_check = ['_staging/patterns', '_staging/lighthouses']
    else:
        filepath = sys.argv[1]
        all_ids = get_all_entity_ids(base_dir)
        errors = validate_entity(filepath, all_ids)
        
        if errors:
            print(f"Validation errors for {filepath}:")
            for error in errors:
                print(f"  {error}")
            sys.exit(1)
        else:
            print(f"✅ {filepath} is valid")
            sys.exit(0)
    
    all_ids = get_all_entity_ids(base_dir)
    total_errors = 0
    total_warnings = 0
    files_checked = 0
    
    for subdir in dirs_to_check:
        dir_path = base_dir / subdir
        if not dir_path.exists():
            continue
        
        for filepath in sorted(dir_path.glob('*.md')):
            files_checked += 1
            errors = validate_entity(str(filepath), all_ids)
            if errors:
                print(f"\n{filepath.name}:")
                for error in errors:
                    print(f"  {error}")
                    if error.severity == 'error':
                        total_errors += 1
                    else:
                        total_warnings += 1
    
    print(f"\n{'='*50}")
    print(f"Files checked: {files_checked}")
    print(f"Total: {total_errors} errors, {total_warnings} warnings")
    
    sys.exit(1 if total_errors > 0 else 0)


if __name__ == '__main__':
    main()

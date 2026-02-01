#!/usr/bin/env python3
"""
Build embeddings index for semantic search of patterns.

This script:
1. Reads all patterns from _patterns/
2. Generates embeddings using OpenAI text-embedding-3-small
3. Saves embeddings to data/embeddings.json for semantic search

Usage:
    python3 scripts/build_embeddings.py

Requirements:
    pip install openai

Environment:
    OPENAI_API_KEY must be set
"""
import os
import json
import yaml
import time
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple, Optional

# Check for OpenAI
try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False
    print("Warning: openai package not installed. Run: pip install openai")

# Configuration
REPO_ROOT = Path(__file__).parent.parent
PATTERNS_DIR = REPO_ROOT / "_patterns"
OUTPUT_FILE = REPO_ROOT / "data" / "embeddings.json"
EMBEDDING_MODEL = "gpt-4.1-nano"  # Using available model for embeddings via compatible API
BATCH_SIZE = 100  # Process in batches to avoid rate limits


def extract_text_for_embedding(filepath: Path) -> Tuple[Optional[str], Optional[Dict]]:
    """Extract text content from a pattern file for embedding."""
    try:
        content = filepath.read_text()
    except Exception as e:
        return None, None
    
    if not content.startswith('---'):
        return None, None
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, None
    
    try:
        frontmatter = yaml.safe_load(parts[1])
        if not frontmatter or 'id' not in frontmatter:
            return None, None
    except yaml.YAMLError:
        return None, None
    
    body = parts[2].strip()
    
    # Create embedding text: title + aliases + first ~2000 chars of body
    title = frontmatter.get('title', '')
    aliases = frontmatter.get('aliases', [])
    aliases_text = ', '.join(aliases) if aliases else ''
    
    # Combine for embedding
    text_parts = [title]
    if aliases_text:
        text_parts.append(f"Also known as: {aliases_text}")
    
    # Add body content (truncated)
    if body:
        # Take first ~2000 chars to stay within token limits
        body_truncated = body[:2000]
        text_parts.append(body_truncated)
    
    embedding_text = '\n\n'.join(text_parts)
    
    metadata = {
        'id': frontmatter.get('id', ''),
        'slug': frontmatter.get('slug', filepath.stem),
        'title': title,
        'domain': frontmatter.get('tags', {}).get('domain', '') if isinstance(frontmatter.get('tags'), dict) else '',
        'filepath': str(filepath.relative_to(REPO_ROOT))
    }
    
    return embedding_text, metadata


def get_embeddings_batch(client: 'OpenAI', texts: List[str]) -> List[List[float]]:
    """Get embeddings for a batch of texts."""
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts
    )
    return [item.embedding for item in response.data]


def build_embeddings():
    """Build embeddings for all patterns."""
    if not HAS_OPENAI:
        print("Error: openai package required. Install with: pip install openai")
        return None
    
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set")
        return None
    
    client = OpenAI()
    
    print("Building embeddings index...")
    print(f"Model: {EMBEDDING_MODEL}")
    
    # Collect all patterns
    patterns_data = []
    
    if PATTERNS_DIR.exists():
        for filepath in sorted(PATTERNS_DIR.glob("*.md")):
            text, metadata = extract_text_for_embedding(filepath)
            if text and metadata:
                patterns_data.append({
                    'text': text,
                    'metadata': metadata
                })
    
    print(f"Found {len(patterns_data)} patterns to embed")
    
    # Process in batches
    embeddings_index = {
        'version': '1.0',
        'generated': datetime.utcnow().isoformat() + 'Z',
        'model': EMBEDDING_MODEL,
        'dimension': 1536,  # text-embedding-3-small dimension
        'total_patterns': len(patterns_data),
        'embeddings': []
    }
    
    for i in range(0, len(patterns_data), BATCH_SIZE):
        batch = patterns_data[i:i + BATCH_SIZE]
        texts = [p['text'] for p in batch]
        
        print(f"Processing batch {i // BATCH_SIZE + 1}/{(len(patterns_data) + BATCH_SIZE - 1) // BATCH_SIZE}...")
        
        try:
            embeddings = get_embeddings_batch(client, texts)
            
            for j, emb in enumerate(embeddings):
                embeddings_index['embeddings'].append({
                    'id': batch[j]['metadata']['id'],
                    'slug': batch[j]['metadata']['slug'],
                    'title': batch[j]['metadata']['title'],
                    'domain': batch[j]['metadata']['domain'],
                    'filepath': batch[j]['metadata']['filepath'],
                    'embedding': emb
                })
            
            # Small delay to avoid rate limits
            if i + BATCH_SIZE < len(patterns_data):
                time.sleep(0.5)
                
        except Exception as e:
            print(f"Error processing batch: {e}")
            continue
    
    return embeddings_index


def save_embeddings(embeddings_index: Dict):
    """Save embeddings to disk."""
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(embeddings_index, f)
    
    # Also save a compact version without embeddings for quick loading
    compact = {
        'version': embeddings_index['version'],
        'generated': embeddings_index['generated'],
        'model': embeddings_index['model'],
        'total_patterns': embeddings_index['total_patterns'],
        'patterns': [
            {
                'id': e['id'],
                'slug': e['slug'],
                'title': e['title'],
                'domain': e['domain']
            }
            for e in embeddings_index['embeddings']
        ]
    }
    
    compact_file = OUTPUT_FILE.parent / 'embeddings_index.json'
    with open(compact_file, 'w') as f:
        json.dump(compact, f, indent=2)
    
    print(f"\nEmbeddings saved to: {OUTPUT_FILE}")
    print(f"Compact index saved to: {compact_file}")
    print(f"File size: {OUTPUT_FILE.stat().st_size / 1024 / 1024:.2f} MB")


def main():
    embeddings_index = build_embeddings()
    
    if embeddings_index:
        save_embeddings(embeddings_index)
        
        print(f"\n{'=' * 60}")
        print("EMBEDDINGS BUILD COMPLETE")
        print(f"{'=' * 60}")
        print(f"Total patterns embedded: {embeddings_index['total_patterns']}")
        print(f"Embedding dimension: {embeddings_index['dimension']}")
    else:
        print("\nEmbeddings build failed. Check errors above.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
TypeID Generator for Commons OS Pattern Engine

Usage:
    python3 generate_typeid.py                    # Generate a pattern TypeID
    python3 generate_typeid.py --type lighthouse  # Generate a lighthouse TypeID
    python3 generate_typeid.py -n 10              # Generate 10 TypeIDs

TypeIDs are based on UUID7 (time-ordered UUIDs) with a prefix:
- 'pat_' for patterns
- 'lh_' for lighthouses
"""

import sys
import uuid
import time


def uuid7():
    """
    Generate a UUID7 (time-ordered UUID).
    
    UUID7 structure:
    - 48 bits: Unix timestamp in milliseconds
    - 4 bits: Version (7)
    - 12 bits: Random
    - 2 bits: Variant
    - 62 bits: Random
    """
    # Get current timestamp in milliseconds
    timestamp_ms = int(time.time() * 1000)
    
    # Create the UUID bytes
    # First 6 bytes: timestamp
    timestamp_bytes = timestamp_ms.to_bytes(6, byteorder='big')
    
    # Generate random bytes for the rest
    random_bytes = uuid.uuid4().bytes[6:]
    
    # Combine timestamp and random bytes
    uuid_bytes = bytearray(timestamp_bytes + random_bytes)
    
    # Set version to 7 (bits 48-51)
    uuid_bytes[6] = (uuid_bytes[6] & 0x0F) | 0x70
    
    # Set variant to RFC 4122 (bits 64-65)
    uuid_bytes[8] = (uuid_bytes[8] & 0x3F) | 0x80
    
    return uuid.UUID(bytes=bytes(uuid_bytes))


def generate_typeid(entity_type='pattern'):
    """Generate a TypeID for a pattern or lighthouse."""
    u = uuid7()
    hex_str = u.hex
    prefix = 'pat' if entity_type == 'pattern' else 'lh'
    return f"{prefix}_{hex_str[:26]}"


def main():
    count = 1
    entity_type = 'pattern'
    
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == '-n' and i + 1 < len(args):
            try:
                count = int(args[i + 1])
                i += 2
            except ValueError:
                print("Error: -n requires an integer argument")
                sys.exit(1)
        elif args[i] == '--type' and i + 1 < len(args):
            if args[i + 1] in ['pattern', 'lighthouse']:
                entity_type = args[i + 1]
                i += 2
            else:
                print("Error: --type must be 'pattern' or 'lighthouse'")
                sys.exit(1)
        elif args[i] in ['-h', '--help']:
            print(__doc__)
            sys.exit(0)
        else:
            i += 1
    
    for _ in range(count):
        print(generate_typeid(entity_type))


if __name__ == '__main__':
    main()

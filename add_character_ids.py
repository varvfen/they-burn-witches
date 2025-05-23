#!/usr/bin/env python3
"""
Simple Character ID Migration Script
===================================

Adds ID field to all character JSON files based on their filename.
Since filenames are already clean (using underscores), this is straightforward.
"""

import os
import json

CHAR_FOLDER = "characters"

def add_ids_to_characters():
    """Add ID field to all character files based on filename."""

    if not os.path.exists(CHAR_FOLDER):
        print(f"❌ Characters folder not found: {CHAR_FOLDER}")
        return

    # Get all JSON files
    json_files = [f for f in os.listdir(CHAR_FOLDER) if f.endswith('.json')]

    if not json_files:
        print(f"❌ No JSON files found in {CHAR_FOLDER}")
        return

    print(f"Found {len(json_files)} character files to update:")
    print()

    updated_count = 0
    skipped_count = 0

    for filename in json_files:
        filepath = os.path.join(CHAR_FOLDER, filename)

        try:
            # Load the character data
            with open(filepath, 'r', encoding='utf-8') as f:
                char_data = json.load(f)

            # Generate ID from filename (remove .json extension)
            character_id = filename.replace('.json', '')

            # Check if ID already exists
            if 'id' in char_data:
                print(f"⏭️  {filename} - ID already exists: {char_data['id']}")
                skipped_count += 1
                continue

            # Add ID at the beginning of the data
            updated_data = {'id': character_id}
            updated_data.update(char_data)

            # Write back to file
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(updated_data, f, indent=2, ensure_ascii=False)

            print(f"✅ {filename} - Added ID: {character_id}")
            updated_count += 1

        except json.JSONDecodeError as e:
            print(f"❌ {filename} - Invalid JSON: {e}")
        except Exception as e:
            print(f"❌ {filename} - Error: {e}")

    print()
    print(f"📊 Summary:")
    print(f"   Updated: {updated_count}")
    print(f"   Skipped: {skipped_count}")
    print(f"   Total: {len(json_files)}")

if __name__ == "__main__":
    print("🔄 Starting Character ID Migration...")
    print("=" * 50)
    add_ids_to_characters()
    print("=" * 50)
    print("✨ Migration complete!")
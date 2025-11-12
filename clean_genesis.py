#!/usr/bin/env python3
"""Remove original English text from Genesis translation"""

import json

# Load the translated Genesis
with open('/home/user/Bible-kjv/Genesis.json', 'r', encoding='utf-8') as f:
    genesis = json.load(f)

# Remove 'original' field from all verses
for chapter in genesis['chapters']:
    for verse in chapter['verses']:
        if 'original' in verse:
            del verse['original']

# Save cleaned version
with open('/home/user/Bible-kjv/Genesis.json', 'w', encoding='utf-8') as f:
    json.dump(genesis, f, ensure_ascii=False, indent=2)

print("✓ Removed all English text from Genesis.json")
print(f"✓ Language: {genesis['language']}")
print(f"✓ Total chapters: {len(genesis['chapters'])}")

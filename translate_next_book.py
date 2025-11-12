#!/usr/bin/env python3
"""Translate next Bible book using SanSum-Gamma"""

import json
import sys
sys.path.insert(0, '/home/user/Bible-kjv')

from sanskrit_sumerian_generator import SanSumGamma, BibleTranslator

def translate_book(book_name):
    """Translate a complete Bible book"""
    input_file = f'/home/user/Bible-kjv/{book_name}.json'
    output_file = f'/home/user/Bible-kjv/{book_name}_Translated.json'
    backup_file = f'/home/user/Bible-kjv/{book_name}_Original_English.json'

    print(f"Translating {book_name} using SanSum-Gamma...")

    # Load original book
    with open(input_file, 'r', encoding='utf-8') as f:
        book_data = json.load(f)

    # Backup original
    with open(backup_file, 'w', encoding='utf-8') as f:
        json.dump(book_data, f, ensure_ascii=False, indent=2)
    print(f"✓ Backed up original to {backup_file}")

    # Create translator
    language = SanSumGamma()
    translator = BibleTranslator(language)

    # Translate all chapters
    translated_chapters = []
    total_chapters = len(book_data['chapters'])

    for i, chapter in enumerate(book_data['chapters'], 1):
        print(f"  Translating Chapter {chapter['chapter']} ({i}/{total_chapters})...")
        translated_chapter = translator.translate_chapter(chapter)

        # Remove 'original' field from verses
        for verse in translated_chapter['verses']:
            if 'original' in verse:
                del verse['original']

        translated_chapters.append(translated_chapter)

    # Create output structure
    output = {
        'book': book_data['book'],
        'language': language.variant_name,
        'description': f"{book_data['book']} translated into {language.variant_name} hybrid language",
        'note': 'Text is continuous without spaces. Punctuation marks sentence boundaries.',
        'chapters': translated_chapters
    }

    # Save translated version
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    # Replace original with translated
    with open(input_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"✓ Translation complete: {book_name}.json")
    print(f"✓ Total chapters translated: {total_chapters}")

    # Show sample
    print(f"\n{'='*80}")
    print(f"SAMPLE: {book_name} Chapter 1, Verses 1-3")
    print(f"{'='*80}")
    for verse in output['chapters'][0]['verses'][:3]:
        print(f"\n{book_name} 1:{verse['verse']}")
        print(verse['text'])
    print(f"{'='*80}")

    return output_file

if __name__ == '__main__':
    book = sys.argv[1] if len(sys.argv) > 1 else 'Exodus'
    translate_book(book)

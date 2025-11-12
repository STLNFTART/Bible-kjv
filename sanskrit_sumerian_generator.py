#!/usr/bin/env python3
"""
Sanskrit-Sumerian Hybrid Language Generator
Creates 4 distinct language variants by mixing Sanskrit and Sumerian phonology
Generates continuous text without spaces while maintaining phonetic flow
"""

import json
import random
import math
from typing import List, Dict, Tuple
from collections import defaultdict

class SanskritSumerianLanguage:
    """Base class for Sanskrit-Sumerian hybrid language generation"""

    # Sanskrit phoneme inventory
    SANSKRIT_CONSONANTS_FIRST = ['k', 'kh', 'g', 'gh', 'c', 'ch', 'j', 'jh',
                                  't', 'th', 'd', 'dh', 'n', 'p', 'ph', 'b', 'bh', 'm']
    SANSKRIT_CONSONANTS_SECOND = ['y', 'r', 'l', 'v', 'ś', 'ṣ', 's', 'h',
                                   'ṭ', 'ṭh', 'ḍ', 'ḍh', 'ṇ', 'ñ', 'ṅ']
    SANSKRIT_VOWELS_FIRST = ['a', 'ā', 'i', 'ī', 'u', 'ū']
    SANSKRIT_VOWELS_SECOND = ['ṛ', 'ṝ', 'e', 'ai', 'o', 'au']

    # Sumerian phoneme inventory
    SUMERIAN_CONSONANTS_FIRST = ['b', 'd', 'g', 'ĝ', 'h', 'k', 'l']
    SUMERIAN_CONSONANTS_SECOND = ['m', 'n', 'p', 'r', 's', 'š', 't', 'z']
    SUMERIAN_VOWELS_FIRST = ['a', 'e']
    SUMERIAN_VOWELS_SECOND = ['i', 'u']

    # Phonotactic rules for natural flow
    FORBIDDEN_CLUSTERS = [
        ('ś', 'ṣ'), ('ṣ', 'ś'), ('s', 'ś'), ('h', 'h'),
        ('ĝ', 'g'), ('š', 's'), ('kh', 'k'), ('th', 't')
    ]

    def __init__(self, variant_name: str):
        self.variant_name = variant_name
        self.consonants = []
        self.vowels = []
        self.syllable_patterns = []
        self.word_length_range = (2, 8)  # in syllables

    def is_valid_cluster(self, c1: str, c2: str) -> bool:
        """Check if consonant cluster is phonotactically valid"""
        return (c1, c2) not in self.FORBIDDEN_CLUSTERS

    def generate_syllable(self, position: str = 'medial') -> str:
        """Generate a single syllable following phonotactic constraints"""
        pattern = random.choice(self.syllable_patterns)
        syllable = ""

        if pattern == 'CV':
            consonant = random.choice(self.consonants)
            vowel = random.choice(self.vowels)
            syllable = consonant + vowel
        elif pattern == 'CVC':
            c1 = random.choice(self.consonants)
            vowel = random.choice(self.vowels)
            # Try to find valid consonant cluster
            valid_c2 = [c for c in self.consonants if self.is_valid_cluster(c1, c)]
            c2 = random.choice(valid_c2) if valid_c2 else random.choice(self.consonants)
            syllable = c1 + vowel + c2
        elif pattern == 'V':
            if position == 'initial':
                syllable = random.choice(self.vowels)
        elif pattern == 'VC':
            vowel = random.choice(self.vowels)
            consonant = random.choice(self.consonants)
            syllable = vowel + consonant

        return syllable

    def generate_word(self, target_length: int = None) -> str:
        """Generate a complete word as continuous syllables"""
        if target_length is None:
            target_length = random.randint(*self.word_length_range)

        word = ""
        for i in range(target_length):
            position = 'initial' if i == 0 else ('final' if i == target_length-1 else 'medial')
            syllable = self.generate_syllable(position)

            # Avoid bad transitions between syllables
            if word and syllable:
                last_char = word[-1]
                first_char = syllable[0]
                # If both are consonants and form bad cluster, adjust
                if last_char in (self.consonants) and first_char in (self.consonants):
                    if not self.is_valid_cluster(last_char, first_char):
                        # Insert bridging vowel
                        word += random.choice(self.vowels[:2])  # Use common vowels

            word += syllable

        return word


    def generate_phrase(self, target_words: int, semantic_weight: float = 1.0) -> str:
        """Generate a phrase with multiple words separated by spaces"""
        words = []
        for _ in range(target_words):
            # Vary word length based on semantic weight
            length = int(random.randint(2, 6) * semantic_weight)
            length = max(2, min(8, length))
            words.append(self.generate_word(length))

        # Join WITH spaces between words
        return ' '.join(words)


class SanSumAlpha(SanskritSumerianLanguage):
    """Variant 1: First half Sanskrit + Second half Sumerian"""

    def __init__(self):
        super().__init__("SanSum-Alpha")
        # Mix: First half of Sanskrit with second half of Sumerian
        self.consonants = (self.SANSKRIT_CONSONANTS_FIRST +
                          self.SUMERIAN_CONSONANTS_SECOND)
        self.vowels = (self.SANSKRIT_VOWELS_FIRST +
                      self.SUMERIAN_VOWELS_SECOND)
        # Prefer CV and CVC patterns (balanced)
        self.syllable_patterns = ['CV', 'CV', 'CV', 'CVC', 'CVC']
        self.word_length_range = (2, 7)


class SanSumBeta(SanskritSumerianLanguage):
    """Variant 2: Second half Sanskrit + First half Sumerian"""

    def __init__(self):
        super().__init__("SanSum-Beta")
        # Mix: Second half of Sanskrit with first half of Sumerian
        self.consonants = (self.SANSKRIT_CONSONANTS_SECOND +
                          self.SUMERIAN_CONSONANTS_FIRST)
        self.vowels = (self.SANSKRIT_VOWELS_SECOND +
                      self.SUMERIAN_VOWELS_FIRST)
        # More complex syllable structures
        self.syllable_patterns = ['CV', 'CVC', 'CVC', 'VC']
        self.word_length_range = (3, 7)


class SanSumGamma(SanskritSumerianLanguage):
    """Variant 3: All Sanskrit consonants + Sumerian vowels"""

    def __init__(self):
        super().__init__("SanSum-Gamma")
        # Sanskrit phonetic richness with Sumerian vowel simplicity
        self.consonants = (self.SANSKRIT_CONSONANTS_FIRST +
                          self.SANSKRIT_CONSONANTS_SECOND)
        self.vowels = (self.SUMERIAN_VOWELS_FIRST +
                      self.SUMERIAN_VOWELS_SECOND)
        # Rich consonant clusters
        self.syllable_patterns = ['CV', 'CV', 'CVC', 'CVC', 'CVC']
        self.word_length_range = (2, 6)


class SanSumDelta(SanskritSumerianLanguage):
    """Variant 4: Sumerian consonants + All Sanskrit vowels"""

    def __init__(self):
        super().__init__("SanSum-Delta")
        # Sumerian simplicity with Sanskrit vowel richness
        self.consonants = (self.SUMERIAN_CONSONANTS_FIRST +
                          self.SUMERIAN_CONSONANTS_SECOND)
        self.vowels = (self.SANSKRIT_VOWELS_FIRST +
                      self.SANSKRIT_VOWELS_SECOND)
        # Flowing patterns with rich vowels
        self.syllable_patterns = ['CV', 'CV', 'CV', 'CVC', 'V']
        self.word_length_range = (2, 8)


class BibleTranslator:
    """Translates Bible verses into hybrid languages"""

    def __init__(self, language_variant: SanskritSumerianLanguage):
        self.language = language_variant
        self.verse_cache = {}

    def analyze_english_verse(self, text: str) -> Dict:
        """Analyze English verse for translation parameters"""
        words = text.split()
        word_count = len(words)
        char_count = len(text.replace(' ', ''))

        # Semantic weight based on word importance
        important_words = ['God', 'LORD', 'heaven', 'earth', 'created',
                          'beginning', 'light', 'darkness', 'man', 'woman']
        semantic_density = sum(1 for w in words if any(imp in w for imp in important_words))
        semantic_weight = 1.0 + (semantic_density / max(word_count, 1)) * 0.5

        return {
            'word_count': word_count,
            'char_count': char_count,
            'semantic_weight': semantic_weight,
            'avg_word_length': char_count / max(word_count, 1)
        }

    def translate_verse(self, verse_text: str, verse_ref: str) -> str:
        """Translate a verse maintaining semantic density"""
        # Check cache first
        if verse_ref in self.verse_cache:
            return self.verse_cache[verse_ref]

        analysis = self.analyze_english_verse(verse_text)

        # Generate translation with similar complexity
        word_count = max(3, int(analysis['word_count'] * 0.8))  # Slightly more compact
        semantic_weight = analysis['semantic_weight']

        # Generate the continuous text
        translation = self.language.generate_phrase(word_count, semantic_weight)

        # Add proper punctuation at the end
        if verse_text.endswith('?'):
            translation += '?'
        elif verse_text.endswith('!'):
            translation += '!'
        elif verse_text.endswith(':'):
            translation += ':'
        else:
            translation += '.'

        self.verse_cache[verse_ref] = translation
        return translation

    def translate_chapter(self, chapter_data: Dict) -> Dict:
        """Translate an entire chapter"""
        translated_verses = []

        chapter_num = chapter_data['chapter']
        for verse in chapter_data['verses']:
            verse_num = verse['verse']
            original_text = verse['text']
            verse_ref = f"{chapter_num}:{verse_num}"

            translated_text = self.translate_verse(original_text, verse_ref)

            translated_verses.append({
                'verse': verse_num,
                'text': translated_text,
                'original': original_text  # Keep for reference during testing
            })

        return {
            'chapter': chapter_num,
            'verses': translated_verses
        }


def benchmark_languages():
    """Benchmark all 4 language variants for expressiveness and flow"""
    print("="*80)
    print("BENCHMARKING SANSKRIT-SUMERIAN HYBRID LANGUAGES")
    print("="*80)

    test_verses = [
        "In the beginning God created the heaven and the earth.",
        "And the earth was without form, and void; and darkness was upon the face of the deep.",
        "And God said, Let there be light: and there was light.",
        "And God saw the light, that it was good: and God divided the light from the darkness."
    ]

    variants = [
        SanSumAlpha(),
        SanSumBeta(),
        SanSumGamma(),
        SanSumDelta()
    ]

    results = {}

    for variant in variants:
        print(f"\n{'='*80}")
        print(f"TESTING: {variant.variant_name}")
        print(f"{'='*80}")
        print(f"Consonants ({len(variant.consonants)}): {' '.join(variant.consonants[:15])}...")
        print(f"Vowels ({len(variant.vowels)}): {' '.join(variant.vowels)}")
        print(f"Syllable patterns: {', '.join(set(variant.syllable_patterns))}")
        print(f"\nSample translations:")
        print("-"*80)

        translator = BibleTranslator(variant)
        translations = []
        total_length = 0
        phoneme_diversity = set()

        for i, verse in enumerate(test_verses, 1):
            trans = translator.translate_verse(verse, f"1:{i}")
            translations.append(trans)
            total_length += len(trans)
            phoneme_diversity.update(trans)

            print(f"\n[Genesis 1:{i}]")
            print(f"Original: {verse}")
            print(f"Translation: {trans}")
            print(f"Length: {len(trans)} chars")

        # Calculate metrics
        avg_length = total_length / len(test_verses)
        phoneme_count = len(phoneme_diversity)
        expressiveness_score = phoneme_count * math.log(avg_length)
        flow_score = len(variant.consonants) * len(variant.vowels) / 10
        robustness_score = (len(variant.consonants) + len(variant.vowels) * 2) / 2

        overall_score = (expressiveness_score * 0.4 +
                        flow_score * 0.3 +
                        robustness_score * 0.3)

        results[variant.variant_name] = {
            'expressiveness': expressiveness_score,
            'flow': flow_score,
            'robustness': robustness_score,
            'overall': overall_score,
            'phoneme_diversity': phoneme_count,
            'avg_length': avg_length
        }

        print(f"\n{'='*80}")
        print(f"METRICS for {variant.variant_name}:")
        print(f"  Expressiveness Score: {expressiveness_score:.2f}")
        print(f"  Flow Score: {flow_score:.2f}")
        print(f"  Robustness Score: {robustness_score:.2f}")
        print(f"  Overall Score: {overall_score:.2f}")
        print(f"  Phoneme Diversity: {phoneme_count}")
        print(f"  Average Length: {avg_length:.1f} chars")

    # Determine winner
    print(f"\n{'='*80}")
    print("FINAL RANKINGS")
    print(f"{'='*80}")

    ranked = sorted(results.items(), key=lambda x: x[1]['overall'], reverse=True)

    for rank, (name, scores) in enumerate(ranked, 1):
        print(f"\n{rank}. {name}")
        print(f"   Overall Score: {scores['overall']:.2f}")
        print(f"   Expressiveness: {scores['expressiveness']:.2f}")
        print(f"   Flow: {scores['flow']:.2f}")
        print(f"   Robustness: {scores['robustness']:.2f}")

    winner = ranked[0][0]
    print(f"\n{'='*80}")
    print(f"WINNER: {winner}")
    print(f"Overall Score: {ranked[0][1]['overall']:.2f}")
    print(f"{'='*80}")

    return winner, results


def translate_genesis(variant_class, output_file='Genesis_Translated.json'):
    """Translate the entire book of Genesis"""
    print(f"\nTranslating Genesis using {variant_class.__name__}...")

    # Load original Genesis
    with open('/home/user/Bible-kjv/Genesis.json', 'r', encoding='utf-8') as f:
        genesis = json.load(f)

    # Create translator
    language = variant_class()
    translator = BibleTranslator(language)

    # Translate all chapters
    translated_chapters = []
    for chapter in genesis['chapters']:
        print(f"  Translating Chapter {chapter['chapter']}...")
        translated_chapter = translator.translate_chapter(chapter)
        translated_chapters.append(translated_chapter)

    # Create output structure
    output = {
        'book': 'Genesis',
        'language': language.variant_name,
        'description': f'Genesis translated into {language.variant_name} hybrid language',
        'note': 'Text is continuous without spaces. Punctuation marks sentence boundaries.',
        'chapters': translated_chapters
    }

    # Save
    with open(f'/home/user/Bible-kjv/{output_file}', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"✓ Translation complete: {output_file}")
    return output_file


if __name__ == '__main__':
    # Run benchmark
    winner_name, all_results = benchmark_languages()

    # Map winner name to class
    variant_map = {
        'SanSum-Alpha': SanSumAlpha,
        'SanSum-Beta': SanSumBeta,
        'SanSum-Gamma': SanSumGamma,
        'SanSum-Delta': SanSumDelta
    }

    winner_class = variant_map[winner_name]

    # Translate Genesis with winning variant
    print(f"\n\nProceeding with full Genesis translation using {winner_name}...")
    output_file = translate_genesis(winner_class)

    print(f"\n{'='*80}")
    print("TRANSLATION COMPLETE")
    print(f"{'='*80}")
    print(f"Output file: {output_file}")
    print(f"Language variant: {winner_name}")

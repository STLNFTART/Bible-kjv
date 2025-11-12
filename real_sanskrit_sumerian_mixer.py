#!/usr/bin/env python3
"""
Real Sanskrit-Sumerian Language Mixer
Mixes actual Sanskrit and Sumerian words to create hybrid sentences
"""

import json
import random
from typing import List, Dict

# Real Sanskrit vocabulary (Devanagari transliterated)
SANSKRIT_VOCAB = {
    'god': ['deva', 'īśvara', 'bhagavān'],
    'lord': ['prabhu', 'svāmin', 'nātha'],
    'heaven': ['svarga', 'dyau', 'naka'],
    'earth': ['pṛthivī', 'bhūmi', 'dharā'],
    'create': ['sṛj', 'nirmā', 'kṛ'],
    'beginning': ['ādi', 'prārambha', 'ārambha'],
    'light': ['jyotis', 'prakāśa', 'dīpti'],
    'darkness': ['tamas', 'andhakāra', 'timira'],
    'water': ['jala', 'udaka', 'ap'],
    'spirit': ['ātman', 'prāṇa', 'manas'],
    'day': ['dina', 'divasa', 'ahar'],
    'night': ['rātri', 'niśā', 'rājani'],
    'man': ['manuṣya', 'nara', 'puruṣa'],
    'woman': ['strī', 'nārī', 'yoṣit'],
    'see': ['paś', 'dṛś', 'lok'],
    'say': ['vac', 'brū', 'kathay'],
    'good': ['śubha', 'sādhu', 'sundara'],
    'make': ['kṛ', 'vidh', 'nirmā'],
    'be': ['as', 'bhū', 'vṛt'],
    'come': ['ā-gam', 'āyā', 'prāp'],
    'go': ['gam', 'yā', 'vraj'],
    'great': ['mahā', 'bṛhat', 'viśāla'],
    'all': ['sarva', 'viśva', 'sakala'],
    'in': ['antar', 'madhye'],
    'from': ['tas', 'prabhṛti'],
    'and': ['ca', 'tathā', 'api'],
    'the': ['sa', 'eṣa', 'tad'],
    'of': ['asya', 'sya'],
    'to': ['prati', 'abhimukham'],
    'he': ['sa', 'ayam', 'eṣa'],
    'call': ['hve', 'āhva', 'nam'],
    'son': ['putra', 'suta', 'ātmaja'],
    'people': ['jana', 'loka', 'prajā'],
    'king': ['rāja', 'nṛpa', 'bhūpati'],
    'house': ['gṛha', 'sadana', 'geh'],
    'land': ['deśa', 'pradeśa', 'bhū'],
    'life': ['jīvana', 'prāṇa', 'āyus'],
    'death': ['mṛtyu', 'maraṇa', 'kāla'],
    'live': ['jīv', 'vṛt', 'vas'],
    'die': ['mṛ', 'pralī', 'kāl'],
    'let': ['anujñā', 'dā'],
    'there': ['tatra', 'atra'],
    'without': ['vinā', 'rahita'],
    'form': ['rūpa', 'ākṛti'],
    'void': ['śūnya', 'riktạ'],
    'upon': ['upari', 'par'],
    'face': ['mukha', 'vadana'],
    'deep': ['gambhīra', 'gahana'],
    'move': ['cal', 'gam'],
    'divide': ['vibhaj', 'chid'],
    'evening': ['sāyam', 'sandhyā'],
    'morning': ['prātas', 'uṣas'],
    'first': ['prathama', 'ādya'],
    'second': ['dvitīya', 'dvi'],
    'third': ['tṛtīya', 'tri'],
    'midst': ['madhya', 'antarā'],
    'under': ['adhas', 'nīce'],
    'above': ['upari', 'ūrdhva'],
    'so': ['evam', 'ittham'],
    'together': ['saha', 'saṃyuktam'],
    'one': ['eka', 'prathama'],
    'place': ['sthāna', 'deśa'],
    'dry': ['śuṣka', 'nirjala'],
    'appear': ['prakāś', 'dṛś'],
    'gather': ['saṃgṛh', 'sañcay'],
    'it': ['tat', 'idam'],
    'that': ['yad', 'tad'],
    'which': ['yad', 'yaḥ'],
    'this': ['idam', 'etat'],
    'into': ['antar', 'praviśya'],
    'with': ['saha', 'sahita'],
    'for': ['arthạm', 'kṛte'],
    'unto': ['prati', 'abhimukham'],
    'his': ['tasya', 'asya'],
    'her': ['tasyāḥ', 'asyāḥ'],
    'their': ['teṣām', 'eṣām'],
    'them': ['tān', 'etān'],
    'not': ['na', 'mā'],
    'no': ['na', 'nahi'],
    'two': ['dvi', 'dvau'],
    'out': ['bahis', 'bāhya'],
}

# Real Sumerian vocabulary (cuneiform transliterated)
SUMERIAN_VOCAB = {
    'god': ['dingir', 'an', 'ilum'],
    'lord': ['lugal', 'en', 'ensi'],
    'heaven': ['an', 'anki', 'anu'],
    'earth': ['ki', 'kalam', 'uraš'],
    'create': ['dim', 'dù', 'gag'],
    'beginning': ['sag', 'pa-è'],
    'light': ['zalag', 'ud', 'bànda'],
    'darkness': ['gi6', 'kuku', 'mi'],
    'water': ['a', 'ídim'],
    'spirit': ['lil', 'zi', 'an-zu'],
    'day': ['ud', 'u4'],
    'night': ['gi6', 'ge6'],
    'man': ['lú', 'guruš', 'nitadam'],
    'woman': ['munus', 'sal', 'dam'],
    'see': ['igi-du8', 'bar', 'igi'],
    'say': ['dug4', 'inim', 'e'],
    'good': ['silim', 'du10', 'dùg'],
    'make': ['dù', 'gag', 'dim'],
    'be': ['gál', 'me'],
    'come': ['du', 'gin', 'è'],
    'go': ['gen', 'du', 'è'],
    'great': ['gal', 'mah', 'gu-la'],
    'all': ['niĝ', 'šu', 'gištug'],
    'in': ['ša', 'a'],
    'from': ['ta'],
    'and': ['ù', 'u3'],
    'the': ['bi'],
    'of': ['ak'],
    'to': ['šè'],
    'he': ['bi', 'ani'],
    'call': ['mu-ù', 'gu3-dé'],
    'son': ['dumu', 'ibila'],
    'people': ['ukkin', 'ùĝ', 'saĝ'],
    'king': ['lugal', 'ensi'],
    'house': ['é', 'ki-gal'],
    'land': ['kalam', 'kur'],
    'life': ['ti', 'nam-ti'],
    'death': ['úš', 'ug7'],
    'live': ['ti', 'til'],
    'die': ['ug7', 'úš'],
    'let': ['he-me', 'gá'],
    'there': ['ne', 'ni'],
    'without': ['nu', 'ul'],
    'form': ['giš-hur', 'alan'],
    'void': ['nu-gál', 'bar'],
    'upon': ['ugu', 'šu-ba'],
    'face': ['igi', 'pa'],
    'deep': ['buranun', 'abzu'],
    'move': ['du', 'è'],
    'divide': ['ba', 'sag-ki'],
    'evening': ['sig-ge6', 'murgu'],
    'morning': ['u4-ul-li', 'u4-zal'],
    'first': ['1-kam', 'imin'],
    'second': ['2-kam', 'min'],
    'third': ['3-kam', 'eš'],
    'midst': ['murgu', 'šà'],
    'under': ['ki-ta', 'kur'],
    'above': ['an-ta', 'ugu'],
    'so': ['ga-nam', 'nu-me'],
    'together': ['niĝin', 'ús'],
    'one': ['aš', 'diš'],
    'place': ['ki', 'šà'],
    'dry': ['bad', 'ḫad'],
    'appear': ['suh', 'è'],
    'gather': ['šum', 'gar'],
    'it': ['bi', 'ne'],
    'that': ['iri', 'ne'],
    'which': ['ša', 'lú'],
    'this': ['ne', 'bi'],
    'into': ['šè', 'a'],
    'with': ['ù', 'da'],
    'for': ['mu', 'šè'],
    'unto': ['šè'],
    'his': ['ani', 'bi'],
    'her': ['ani-munus'],
    'their': ['bi-meš'],
    'them': ['bi-ne'],
    'not': ['nu', 'ul'],
    'no': ['nu'],
    'two': ['min'],
    'out': ['è', 'bar'],
}

# Common English to concept mapping
CONCEPT_MAP = {
    'god': 'god', 'lord': 'lord', 'heaven': 'heaven', 'earth': 'earth',
    'create': 'create', 'created': 'create', 'beginning': 'beginning',
    'light': 'light', 'darkness': 'darkness', 'dark': 'darkness',
    'water': 'water', 'waters': 'water', 'spirit': 'spirit',
    'day': 'day', 'night': 'night', 'man': 'man', 'woman': 'woman',
    'see': 'see', 'saw': 'see', 'seen': 'see',
    'say': 'say', 'said': 'say', 'saying': 'say',
    'good': 'good', 'make': 'make', 'made': 'make',
    'be': 'be', 'was': 'be', 'were': 'be', 'been': 'be',
    'come': 'come', 'came': 'come', 'go': 'go', 'went': 'go',
    'great': 'great', 'all': 'all', 'in': 'in', 'from': 'from',
    'and': 'and', 'the': 'the', 'of': 'of', 'to': 'to',
    'he': 'he', 'call': 'call', 'called': 'call',
    'son': 'son', 'sons': 'son', 'people': 'people',
    'king': 'king', 'house': 'house', 'land': 'land',
    'life': 'life', 'death': 'death', 'live': 'live', 'die': 'die',
    'let': 'let', 'there': 'there', 'without': 'without',
    'form': 'form', 'void': 'void', 'upon': 'upon',
    'face': 'face', 'deep': 'deep', 'move': 'move', 'moved': 'move',
    'divide': 'divide', 'divided': 'divide', 'evening': 'evening',
    'morning': 'morning', 'first': 'first', 'second': 'second',
    'third': 'third', 'midst': 'midst', 'under': 'under',
    'above': 'above', 'so': 'so', 'together': 'together',
    'one': 'one', 'place': 'place', 'dry': 'dry',
    'appear': 'appear', 'gather': 'gather', 'gathered': 'gather',
    'it': 'it', 'that': 'that', 'which': 'which',
    'this': 'this', 'into': 'into', 'with': 'with',
    'for': 'for', 'unto': 'unto', 'his': 'his',
    'her': 'her', 'their': 'their', 'them': 'them',
    'not': 'not', 'no': 'no', 'two': 'two',
    'out': 'out',
}


class RealLanguageMixer:
    """Mixes actual Sanskrit and Sumerian words"""

    def __init__(self, sanskrit_ratio: float = 0.5):
        """
        sanskrit_ratio: 0.5 means 50/50 mix, 0.3 means 30% Sanskrit 70% Sumerian
        """
        self.sanskrit_ratio = sanskrit_ratio

    def get_mixed_word(self, english_word: str) -> str:
        """Get a Sanskrit or Sumerian word for an English word"""
        # Normalize the word
        word_lower = english_word.lower().strip('.,;:!?')

        # Find concept
        concept = CONCEPT_MAP.get(word_lower)

        if not concept:
            # Unknown word - create placeholder based on original
            return english_word.lower()

        # Decide Sanskrit or Sumerian
        use_sanskrit = random.random() < self.sanskrit_ratio

        if use_sanskrit and concept in SANSKRIT_VOCAB:
            return random.choice(SANSKRIT_VOCAB[concept])
        elif concept in SUMERIAN_VOCAB:
            return random.choice(SUMERIAN_VOCAB[concept])
        elif concept in SANSKRIT_VOCAB:
            return random.choice(SANSKRIT_VOCAB[concept])
        else:
            return english_word.lower()

    def translate_sentence(self, english_text: str) -> str:
        """Translate a sentence into mixed Sanskrit-Sumerian"""
        # Split into words, preserving punctuation
        words = english_text.replace(',', ' ,').replace('.', ' .').replace(':', ' :').replace(';', ' ;').replace('!', ' !').replace('?', ' ?').split()

        translated_words = []
        for word in words:
            if word in '.,;:!?':
                # Don't add space before punctuation
                if translated_words:
                    translated_words[-1] += word
            else:
                translated_words.append(self.get_mixed_word(word))

        return ' '.join(translated_words)


def translate_book(book_name: str, sanskrit_ratio: float = 0.5):
    """Translate a Bible book using real Sanskrit-Sumerian mix"""
    input_file = f'/home/user/Bible-kjv/{book_name}_Original_English.json'
    output_file = f'/home/user/Bible-kjv/{book_name}.json'

    print(f"Translating {book_name} with {int(sanskrit_ratio*100)}% Sanskrit, {int((1-sanskrit_ratio)*100)}% Sumerian...")

    with open(input_file, 'r', encoding='utf-8') as f:
        book_data = json.load(f)

    mixer = RealLanguageMixer(sanskrit_ratio)

    translated_chapters = []
    for chapter in book_data['chapters']:
        print(f"  Chapter {chapter['chapter']}...")
        translated_verses = []

        for verse in chapter['verses']:
            translated_text = mixer.translate_sentence(verse['text'])
            translated_verses.append({
                'verse': verse['verse'],
                'text': translated_text
            })

        translated_chapters.append({
            'chapter': chapter['chapter'],
            'verses': translated_verses
        })

    output = {
        'book': book_data['book'],
        'language': f'Sanskrit-Sumerian Mix ({int(sanskrit_ratio*100)}/{int((1-sanskrit_ratio)*100)})',
        'description': f'{book_data["book"]} with real Sanskrit and Sumerian words mixed',
        'note': 'Real Sanskrit and Sumerian vocabulary mixed in sentences',
        'chapters': translated_chapters
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"✓ Complete: {output_file}")
    return output_file


if __name__ == '__main__':
    import sys
    book = sys.argv[1] if len(sys.argv) > 1 else 'Genesis'
    ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
    translate_book(book, ratio)

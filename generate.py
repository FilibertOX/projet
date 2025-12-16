#!/usr/bin/env python3
"""
Générateur de fichier avec caractères UTF-8 aléatoires
Supporte différentes distributions pour tester la compression Huffman
"""

import random
import sys

def generate_uniform(charset, num_chars):
    """Distribution uniforme: tous les caractères ont la même probabilité"""
    return [random.choice(charset) for _ in range(num_chars)]

def generate_normal(charset, num_chars):
    """Distribution normale: caractères au milieu plus fréquents"""
    chars = []
    n = len(charset)
    mean = n / 2
    stddev = n / 4

    for _ in range(num_chars):
        index = int(random.gauss(mean, stddev))
        index = max(0, min(n - 1, index))
        chars.append(charset[index])

    return chars

def generate_zipf(charset, num_chars, alpha=1.5):
    """Distribution de Zipf: premiers caractères très fréquents (comme du vrai texte)"""
    n = len(charset)
    weights = [1.0 / ((i + 1) ** alpha) for i in range(n)]
    total = sum(weights)
    probabilities = [w / total for w in weights]
    return random.choices(charset, weights=probabilities, k=num_chars)

def generate_random(ranges, num_chars):
    """Random: choisir aléatoirement dans toutes les plages UTF-8"""
    characters = []
    for _ in range(num_chars):
        start, end = random.choice(ranges)
        try:
            characters.append(chr(random.randint(start, end)))
        except ValueError:
            continue
    return characters

def generate_random_utf8_file(filename, num_chars=1000, distribution='random',
                              include_nonprintable=True, alpha=1.5):
    """Génère un fichier avec des caractères UTF-8 selon une distribution"""

    # Plages de code points UTF-8
    ranges = [
        (0x0020, 0x007E),  # ASCII printable
    ]

    if include_nonprintable:
        ranges.extend([
            (0x0000, 0x001F),  # ASCII control
            (0x007F, 0x009F),  # C1 control
        ])

    ranges.extend([
        (0x00A0, 0x00FF),  # Latin-1 Supplement
        (0x0100, 0x017F),  # Latin Extended-A
        (0x0180, 0x024F),  # Latin Extended-B
        (0x0250, 0x02AF),  # IPA Extensions
        (0x02B0, 0x02FF),  # Spacing Modifier Letters
        (0x0370, 0x03FF),  # Greek and Coptic
        (0x0400, 0x04FF),  # Cyrillic
        (0x0500, 0x052F),  # Cyrillic Supplement
        (0x0530, 0x058F),  # Armenian
        (0x0590, 0x05FF),  # Hebrew
        (0x0600, 0x06FF),  # Arabic
        (0x0700, 0x074F),  # Syriac
        (0x0780, 0x07BF),  # Thaana
        (0x0900, 0x097F),  # Devanagari
        (0x0980, 0x09FF),  # Bengali
        (0x0A00, 0x0A7F),  # Gurmukhi
        (0x0B00, 0x0B7F),  # Oriya
        (0x0C00, 0x0C7F),  # Telugu
        (0x0D00, 0x0D7F),  # Malayalam
        (0x0E00, 0x0E7F),  # Thai
        (0x0E80, 0x0EFF),  # Lao
        (0x0F00, 0x0FFF),  # Tibetan
        (0x1000, 0x109F),  # Myanmar
        (0x10A0, 0x10FF),  # Georgian
        (0x1100, 0x11FF),  # Hangul Jamo
        (0x1200, 0x137F),  # Ethiopic
        (0x13A0, 0x13FF),  # Cherokee
        (0x1680, 0x169F),  # Ogham
        (0x16A0, 0x16FF),  # Runic
        (0x1780, 0x17FF),  # Khmer
        (0x1800, 0x18AF),  # Mongolian
        (0x1E00, 0x1EFF),  # Latin Extended Additional
        (0x1F00, 0x1FFF),  # Greek Extended
        (0x2000, 0x206F),  # General Punctuation
        (0x2070, 0x209F),  # Superscripts and Subscripts
        (0x20A0, 0x20CF),  # Currency Symbols
        (0x2100, 0x214F),  # Letterlike Symbols
        (0x2150, 0x218F),  # Number Forms
        (0x2190, 0x21FF),  # Arrows
        (0x2200, 0x22FF),  # Mathematical Operators
        (0x2300, 0x23FF),  # Miscellaneous Technical
        (0x2400, 0x243F),  # Control Pictures
        (0x2460, 0x24FF),  # Enclosed Alphanumerics
        (0x2500, 0x257F),  # Box Drawing
        (0x2580, 0x259F),  # Block Elements
        (0x25A0, 0x25FF),  # Geometric Shapes
        (0x2600, 0x26FF),  # Miscellaneous Symbols
        (0x2700, 0x27BF),  # Dingbats
        (0x27C0, 0x27EF),  # Miscellaneous Mathematical Symbols-A
        (0x2800, 0x28FF),  # Braille Patterns
        (0x2E80, 0x2EFF),  # CJK Radicals Supplement
        (0x3000, 0x303F),  # CJK Symbols and Punctuation
        (0x3040, 0x309F),  # Hiragana
        (0x30A0, 0x30FF),  # Katakana
        (0x3100, 0x312F),  # Bopomofo
        (0x3130, 0x318F),  # Hangul Compatibility Jamo
        (0x31A0, 0x31BF),  # Bopomofo Extended
        (0x3200, 0x32FF),  # Enclosed CJK Letters and Months
        (0x3300, 0x33FF),  # CJK Compatibility
        (0x4E00, 0x4EFF),  # CJK Unified Ideographs (sample)
        (0x5000, 0x50FF),  # CJK Unified Ideographs (sample)
        (0xAC00, 0xACFF),  # Hangul Syllables (sample)
        (0xFB00, 0xFB4F),  # Alphabetic Presentation Forms
        (0xFB50, 0xFDFF),  # Arabic Presentation Forms-A
        (0xFE20, 0xFE2F),  # Combining Half Marks
        (0xFE30, 0xFE4F),  # CJK Compatibility Forms
        (0xFE50, 0xFE6F),  # Small Form Variants
        (0xFE70, 0xFEFF),  # Arabic Presentation Forms-B
        (0xFF00, 0xFFEF),  # Halfwidth and Fullwidth Forms
        (0x1F300, 0x1F5FF),  # Miscellaneous Symbols and Pictographs
        (0x1F600, 0x1F64F),  # Emoticons
        (0x1F680, 0x1F6FF),  # Transport and Map Symbols
        (0x1F700, 0x1F77F),  # Alchemical Symbols
        (0x1F780, 0x1F7FF),  # Geometric Shapes Extended
        (0x1F800, 0x1F8FF),  # Supplemental Arrows-C
        (0x1F900, 0x1F9FF),  # Supplemental Symbols and Pictographs
    ])

    # Créer charset
    charset = []
    for start, end in ranges:
        sample_size = min(20, end - start + 1)
        for _ in range(sample_size):
            try:
                charset.append(chr(random.randint(start, end)))
            except ValueError:
                continue

    charset = list(set(charset))

    # Générer selon la distribution
    if distribution == 'random':
        characters = generate_random(ranges, num_chars)
    elif distribution == 'uniform':
        characters = generate_uniform(charset, num_chars)
    elif distribution == 'normal':
        characters = generate_normal(charset, num_chars)
    elif distribution == 'zipf':
        characters = generate_zipf(charset, num_chars, alpha)
    else:
        print(f"Erreur: distribution '{distribution}' inconnue")
        sys.exit(1)

    # Écrire fichier
    content = ''.join(characters)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    # Statistiques
    from collections import Counter
    freq = Counter(characters)
    top = freq.most_common(3)

    print(f"✓ Fichier: {filename}")
    print(f"  Caractères: {len(characters)}, Taille: {len(content.encode('utf-8'))} octets")
    print(f"  Distribution: {distribution}, Uniques: {len(charset)}")
    print(f"  Top 3: ", end='')
    for char, count in top:
        pct = (count / len(characters)) * 100
        print(f"{repr(char) if char.isprintable() else 'ctrl'}({pct:.1f}%) ", end='')
    print()

def main():
    if len(sys.argv) < 2 or '--help' in sys.argv:
        print("Usage: python3 generate_random_utf8.py <filename> [options]")
        print("")
        print("Options:")
        print("  --num <N>             Nombre de caractères (défaut: 1000)")
        print("  --random              Aléatoire pur (défaut)")
        print("  --uniform             Distribution uniforme")
        print("  --normal              Distribution normale")
        print("  --zipf [alpha]        Distribution de Zipf (alpha=1.5 défaut)")
        print("  --no-nonprintable     Exclure caractères non-imprimables")
        print("")
        print("Exemples:")
        print("  python3 generate_random_utf8.py test.txt")
        print("  python3 generate_random_utf8.py test.txt --num 5000 --zipf")
        print("  python3 generate_random_utf8.py test.txt --uniform")
        sys.exit(0)

    filename = sys.argv[1]
    num_chars = 10000
    distribution = 'random'
    include_nonprintable = True
    alpha = 1.5

    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]

        if arg == '--num':
            num_chars = int(sys.argv[i + 1])
            i += 2
        elif arg == '--random':
            distribution = 'random'
            i += 1
        elif arg == '--uniform':
            distribution = 'uniform'
            i += 1
        elif arg == '--normal':
            distribution = 'normal'
            i += 1
        elif arg == '--zipf':
            distribution = 'zipf'
            if i + 1 < len(sys.argv) and sys.argv[i + 1].replace('.', '').isdigit():
                alpha = float(sys.argv[i + 1])
                i += 2
            else:
                i += 1
        elif arg == '--no-nonprintable':
            include_nonprintable = False
            i += 1
        else:
            print(f"Argument inconnu: {arg}")
            sys.exit(1)

    generate_random_utf8_file(filename, num_chars, distribution, include_nonprintable, alpha)

if __name__ == '__main__':
    main()

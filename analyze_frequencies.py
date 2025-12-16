#!/usr/bin/env python3
"""
Analyse des fréquences de caractères dans les fichiers
Permet d'étudier la distribution des caractères pour comprendre la compressibilité
"""

import sys
from collections import Counter
from pathlib import Path


def get_character_frequencies(file_path):
    """
    Lit un fichier et renvoie un dictionnaire des fréquences de chaque caractère.

    Args:
        file_path: Chemin vers le fichier à analyser

    Returns:
        dict: Dictionnaire {caractère: fréquence} où fréquence est le nombre d'occurrences
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Compter les occurrences de chaque caractère
        frequencies = Counter(content)

        return dict(frequencies)

    except Exception as e:
        print(f"Erreur lors de la lecture de {file_path}: {e}")
        return {}


def get_character_probabilities(file_path):
    """
    Lit un fichier et renvoie un dictionnaire des probabilités de chaque caractère.

    Args:
        file_path: Chemin vers le fichier à analyser

    Returns:
        dict: Dictionnaire {caractère: probabilité} où probabilité est entre 0 et 1
    """
    frequencies = get_character_frequencies(file_path)

    if not frequencies:
        return {}

    total = sum(frequencies.values())
    probabilities = {char: count / total for char, count in frequencies.items()}

    return probabilities


def display_top_characters(file_path, n=10):
    """
    Affiche les n caractères les plus fréquents dans un fichier.

    Args:
        file_path: Chemin vers le fichier à analyser
        n: Nombre de caractères à afficher (défaut: 10)
    """
    frequencies = get_character_frequencies(file_path)

    if not frequencies:
        print(f"Aucune donnée pour {file_path}")
        return

    total = sum(frequencies.values())

    print(f"\n{'='*70}")
    print(f"Analyse de: {file_path}")
    print(f"{'='*70}")
    print(f"Nombre total de caractères: {total}")
    print(f"Nombre de caractères distincts: {len(frequencies)}")
    print(f"\nTop {n} caractères les plus fréquents:")
    print(f"{'-'*70}")
    print(f"{'Rang':<6} {'Caractère':<15} {'Fréquence':<12} {'Probabilité':<12} {'%':<10}")
    print(f"{'-'*70}")

    # Tri par fréquence décroissante
    sorted_chars = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    for i, (char, freq) in enumerate(sorted_chars[:n], 1):
        prob = freq / total
        percent = prob * 100

        # Affichage spécial pour les caractères non imprimables
        if char == '\n':
            char_display = '\\n (newline)'
        elif char == '\t':
            char_display = '\\t (tab)'
        elif char == ' ':
            char_display = '(espace)'
        elif char == '\r':
            char_display = '\\r (retour)'
        else:
            char_display = repr(char)

        print(f"{i:<6} {char_display:<15} {freq:<12} {prob:<12.6f} {percent:<10.2f}%")

    print(f"{'-'*70}")


def analyze_distribution_type(file_path):
    """
    Analyse le type de distribution des caractères (uniforme, Zipf, etc.).

    Args:
        file_path: Chemin vers le fichier à analyser

    Returns:
        dict: Statistiques sur la distribution
    """
    frequencies = get_character_frequencies(file_path)

    if not frequencies:
        return {}

    total = sum(frequencies.values())
    sorted_freqs = sorted(frequencies.values(), reverse=True)

    # Statistiques
    stats = {
        'total_chars': total,
        'unique_chars': len(frequencies),
        'most_common_freq': sorted_freqs[0],
        'most_common_prob': sorted_freqs[0] / total,
        'least_common_freq': sorted_freqs[-1],
        'least_common_prob': sorted_freqs[-1] / total,
    }

    # Calcul du ratio de concentration (top 10% vs reste)
    top_10_percent_count = max(1, len(sorted_freqs) // 10)
    top_10_percent_sum = sum(sorted_freqs[:top_10_percent_count])
    stats['concentration_ratio'] = top_10_percent_sum / total

    return stats


def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_frequencies.py <fichier> [nombre_top_chars]")
        print("Exemple: python analyze_frequencies.py data/input_file/test_code_python.txt 20")
        sys.exit(1)

    file_path = sys.argv[1]
    n_top = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    if not Path(file_path).exists():
        print(f"Erreur: fichier '{file_path}' introuvable")
        sys.exit(1)

    # Affichage des top caractères
    display_top_characters(file_path, n_top)

    # Affichage des statistiques de distribution
    stats = analyze_distribution_type(file_path)
    print(f"\nStatistiques de distribution:")
    print(f"{'-'*70}")
    print(f"Caractères uniques: {stats['unique_chars']}")
    print(f"Caractère le plus fréquent: {stats['most_common_freq']} ({stats['most_common_prob']*100:.2f}%)")
    print(f"Caractère le moins fréquent: {stats['least_common_freq']} ({stats['least_common_prob']*100:.2f}%)")
    print(f"Ratio de concentration (top 10%): {stats['concentration_ratio']*100:.2f}%")
    print(f"{'='*70}\n")


if __name__ == '__main__':
    main()

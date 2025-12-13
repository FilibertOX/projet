# Projet de Compression de Texte

Ce projet implémente un algorithme de compression de texte basé sur le codage de Huffman adaptatif. Il permet de compresser et décompresser des fichiers texte en utilisant des structures de données arborescentes. Les scripts mesurent également les performances (tailles des fichiers, taux de compression/décompression, temps d'exécution) et les enregistrent dans des fichiers de log.

## Fichiers Principaux

- `compresser.py` : Script principal pour la compression d'un fichier texte, avec logging des métriques.
- `decompresser.py` : Script principal pour la décompression d'un fichier compressé, avec logging des métriques.
- `compresser.sh` : Script shell pour lancer la compression.
- `decompresser.sh` : Script shell pour lancer la décompression.
- `exo2.py` : Fonctions pour la lecture et l'écriture de fichiers binaires.
- `exo3.py` : Implémentation de l'algorithme de compression et décompression.
- `sdd.py` : Structures de données (Arbre, Sdd) utilisées pour le codage.
- `compression.txt` : Fichier de log des compressions (dans `logs/`, créé automatiquement).
- `decompression.txt` : Fichier de log des décompressions (dans `logs/`, créé automatiquement).

## Structure des Dossiers

Le projet organise les fichiers dans des dossiers pour une meilleure gestion :

- `data/InputFile/` : Fichiers texte d'entrée à compresser.
- `data/OutputFileBin/` : Fichiers compressés (.huff).
- `data/OutputFile/` : Fichiers décompressés (optionnel).
- `data/TransitionBin/` : Fichiers intermédiaires (optionnel).
- `logs/` : Fichiers de log des performances (`compression.txt`, `decompression.txt`).

## Utilisation

### Compression

Pour compresser un fichier texte (peut être dans un sous-dossier) :

```bash
./compresser.sh <fichier_entree.txt> <fichier_sortie.huff>
```

Exemple :
```bash
./compresser.sh data/InputFile/Blaise_Pascal.txt data/OutputFileBin/Blaise_Pascal.txt.huff
```

Après compression, les métriques sont ajoutées à `logs/compression.txt`.

### Décompression

Pour décompresser un fichier compressé :

```bash
./decompresser.sh <fichier_entree.huff> <fichier_sortie.txt>
```

Exemple :
```bash
./decompresser.sh data/OutputFileBin/Blaise_Pascal.txt.huff data/OutputFile/decompressed.txt
```

Après décompression, les métriques sont ajoutées à `logs/decompression.txt`.

### Scripts Python Directs

Vous pouvez aussi utiliser les scripts Python directement :

Compression :
```bash
python3 compresser.py <fichier_entree.txt> <fichier_sortie.huff>
```

Décompression :
```bash
python3 decompresser.py <fichier_entree.huff> <fichier_sortie.txt>
```

## Logging des Performances

Chaque exécution de compression ou décompression enregistre automatiquement les informations suivantes dans les fichiers respectifs du dossier `logs/` :

### compression.txt
- Fichier entrée ; Fichier sortie ; Taille entrée ; Taille sortie ; Taux compression ; Temps compression (ms)

### decompression.txt
- Fichier entrée ; Fichier sortie ; Taille entrée ; Taille sortie ; Taux decompression ; Temps decompression (ms)

Le taux est calculé comme taille_sortie / taille_entrée (avec 5 décimales). Les fichiers de log incluent une en-tête la première fois qu'ils sont créés.

## Algorithme

L'algorithme utilise un codage de Huffman adaptatif où l'arbre est construit dynamiquement au fur et à mesure de la lecture du texte. Les caractères déjà rencontrés ont des codes plus courts, tandis que les nouveaux caractères sont encodés avec leur code UTF-8 précédé d'un code spécial.

## Dépendances

- Python 3
- Modules standard : sys, os

## Exécution

Assurez-vous que tous les fichiers sont dans le même répertoire et que les scripts ont les permissions d'exécution :

```bash
chmod +x compresser.sh decompresser.sh
```

## Tests

Des fichiers de test sont présents :
- `Blaise_Pascal.txt` : Fichier texte d'exemple.
- `Blaise_Pascal.txt.huff` : Version compressée.

Pour tester :
1. Compresser : `./compresser.sh Blaise_Pascal.txt test.huff`
2. Décompresser : `./decompresser.sh test.huff test_decomp.txt`
3. Vérifier que `test.huff` est identique à `Blaise_Pascal.txt.huff`
4. Vérifier que `test_decomp.txt` est identique à `Blaise_Pascal.txt`
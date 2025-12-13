# Projet de Compression de Texte

Ce projet implémente un algorithme de compression de texte basé sur le codage de Huffman adaptatif. Il permet de compresser et décompresser des fichiers texte en utilisant des structures de données arborescentes.

## Fichiers Principaux

- `compresser.py` : Script principal pour la compression d'un fichier texte.
- `decompresser.py` : Script principal pour la décompression d'un fichier compressé.
- `compresser.sh` : Script shell pour lancer la compression.
- `decompresser.sh` : Script shell pour lancer la décompression.
- `exo2.py` : Fonctions pour la lecture et l'écriture de fichiers binaires.
- `exo3.py` : Implémentation de l'algorithme de compression et décompression.
- `sdd.py` : Structures de données (Arbre, Sdd) utilisées pour le codage.

## Utilisation

### Compression

Pour compresser un fichier texte :

```bash
./compresser.sh <fichier_entree.txt> <fichier_sortie.huff>
```

Exemple :
```bash
./compresser.sh Blaise_Pascal.txt Blaise_Pascal.txt.huff
```

### Décompression

Pour décompresser un fichier compressé :

```bash
./decompresser.sh <fichier_entree.huff> <fichier_sortie.txt>
```

Exemple :
```bash
./decompresser.sh Blaise_Pascal.txt.huff decompressed.txt
```

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
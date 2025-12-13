import sys
import os
from exo3 import lecture, decompression

def main():
    # Vérification du nombre d'arguments
    if len(sys.argv) != 3:
        print("Usage : python main.py <fichier1> <fichier2>")
        sys.exit(1)

    textO = sys.argv[1]
    textFinal = sys.argv[2]

    # Vérification de l'existence des fichiers
    if not os.path.isfile(textO):
        print(f"Erreur : le fichier '{textO}' n'existe pas.")
        sys.exit(1)

    if not os.path.isfile(textFinal):
        print(f"Erreur : le fichier '{textFinal}' n'existe pas.")
        sys.exit(1)

    res=lecture(textFinal)

    decompressed = decompression(res)

    with open(textFinal, 'w', encoding='utf-8') as f:
        f.write(decompressed)
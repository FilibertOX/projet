import sys
import os
from exo3 import compresion, ecriture

def main():
    # Vérification du nombre d'arguments
    if len(sys.argv) != 3:
        print("Usage : python main.py <fichier1> <fichier2>")
        sys.exit(1)

    textO = sys.argv[1]
    textCBin = sys.argv[2]

    # Vérification de l'existence des fichiers
    if not os.path.isfile(textO):
        print(f"Erreur : le fichier '{textO}' n'existe pas.")
        sys.exit(1)

    textC = 'Blaise_Pascal_binary.txt'

    with open(textO, 'r', encoding='utf-8') as f:
        text_in = f.read()
        print("Texte lu depuis", textO)
        print(text_in)

    compressed = compresion(text_in)

    with open(textC, 'w', encoding='utf-8') as f:
        f.write(compressed)

    ecriture(textC, textCBin)



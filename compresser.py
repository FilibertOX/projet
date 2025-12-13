import sys
import os
import time
from exo3 import compresion, ecriture


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

textC = 'data/TransitionBin/temp_compressed.txt'

input_size = os.path.getsize(textO)

start_time = time.time()

with open(textO, 'r', encoding='utf-8') as f:
    text_in = f.read()

compressed = compresion(text_in)

with open(textC, 'w', encoding='utf-8') as f:
    f.write(compressed)

ecriture(textC, textCBin)

end_time = time.time()
compression_time_ms = (end_time - start_time) * 1000

output_size = os.path.getsize(textCBin)
compression_ratio = output_size / input_size if input_size > 0 else 0

os.makedirs('logs', exist_ok=True)
with open('logs/compression.txt', 'a', encoding='utf-8') as f:
    f.write(f"{textO};{textCBin};{input_size};{output_size};{compression_ratio:.5f};{compression_time_ms:.0f}\n")

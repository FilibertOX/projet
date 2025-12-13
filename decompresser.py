import sys
import os
import time
from exo3 import lecture, decompression

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

input_size = os.path.getsize(textO)

start_time = time.time()

res=lecture(textO)

decompressed = decompression(res)

with open(textFinal, 'w', encoding='utf-8') as f:
    f.write(decompressed)

end_time = time.time()
decompression_time_ms = (end_time - start_time) * 1000

output_size = os.path.getsize(textFinal)
decompression_ratio = output_size / input_size if input_size > 0 else 0

with open('decompression.txt', 'a', encoding='utf-8') as f:
    if os.path.getsize('decompression.txt') == 0:
        f.write("Fichier entrée;Fichier sortie;Taille entrée;Taille sortie;Taux decompression;Temps decompression (ms)\n")
    f.write(f"{textO};{textFinal};{input_size};{output_size};{decompression_ratio:.5f};{decompression_time_ms:.0f}\n")
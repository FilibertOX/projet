import random
import unicodedata
import time
from exo3 import *
from exo2 import *

def generate_random_utf8_text(n,fichier):
    """
    Generate a random UTF-8 text of length n.
    Avoids control characters and unprintable ranges.
    """
    text = []
    f= open(fichier, 'w', encoding='utf-8')
    while len(text) < n:
        # Choose a random Unicode code point
        cp = random.randint(0x20, 0xFFFF)  # BMP range
        
        ch = chr(cp)
        
        # Filter out non-printable or weird control characters
        if unicodedata.category(ch)[0] != "C":  # skip control chars
            text.append(ch)
    f.write(''.join(text))
    f.close()

generate_random_utf8_text(10000,'test_exo4.txt')
"""
textO = 'test_exo4.txt'
textC = 'test_exo4_binary.txt'
textCBin = 'test_exo4.txt.huff'
textFinal = 'test_exo4_2.txt'
with open(textO, 'r', encoding='utf-8') as f:
	text_in = f.read()

debutComp=time.time()
compressed = compresion(text_in)
finComp=time.time()

print("Temps de compression :",finComp - debutComp," secondes")

with open(textC, 'w', encoding='utf-8') as f:
    f.write(compressed)

ecriture(textC, textCBin)

res=lecture(textCBin)

debutDecomp=time.time()
decompressed = decompression(res)
finDecomp=time.time()

print("Temps de décompression :",finDecomp - debutDecomp," secondes")

with open(textFinal, 'w', encoding='utf-8') as f:
	f.write(decompressed)

print("Taux de compression:",len(res)/len(text_in))
"""
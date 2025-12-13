#!/bin/bash
if [ "$#" -ne 2 ]; then
    echo "Usage : $0 <x> <y>"
    exit 1
fi
echo "Decompression de $1 vers $2"
python3 ./decompresser.py "$1" "$2"
echo "Decompression terminée."
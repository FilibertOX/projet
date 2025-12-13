#!/bin/bash
if [ "$#" -ne 2 ]; then
    echo "Usage : $0 <x> <y>"
    exit 1
fi
echo "Compression de $1 vers $2"
python3 ./compresser.py "$1" "$2"
echo "Compression terminée."
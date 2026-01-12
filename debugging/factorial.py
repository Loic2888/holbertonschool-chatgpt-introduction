#!/usr/bin/python3
import sys

def factorial(n):
	result = 1
	while n > 1:
		result *= n
		n -= 1  # ← Ajout crucial : décrémenter n !
	return result

if len(sys.argv) != 2 or not sys.argv[1].isdigit():
	print("Usage: ./script.py <nombre entier positif>", file=sys.stderr)
	sys.exit(1)

f = factorial(int(sys.argv[1]))
print(f)
# Correction apportée : ajout de la ligne "n -= 1" pour décrémenter n à chaque itération.

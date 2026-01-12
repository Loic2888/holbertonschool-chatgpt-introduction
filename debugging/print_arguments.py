#!/usr/bin/python3
import sys

print(f"Nombre d'arguments : {len(sys.argv)}")
print("Arguments :")
for i in range(len(sys.argv)):
	print(f"  sys.argv[{i}] = '{sys.argv[i]}'")

#!/usr/bin/python3
import sys

def factorial(n):
	"""
	Function description:
		Computes the factorial of a non-negative integer n using recursion.

	Parameters:
		n (int): The non-negative integer whose factorial is to be computed.

	Returns:
		int: The factorial of n. If n is 0, returns 1.
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

# Convert the first command-line argument to int and compute its factorial
f = factorial(int(sys.argv[1]))
print(f)

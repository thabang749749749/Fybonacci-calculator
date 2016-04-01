# fybonacci.py
# -*- coding: utf-8 -*-

import sys

# Variables
whiteSpace = "   "
decorator1 = '-' * 35
decorator2 = '-' * 25
decorator3 = '-' * 16
invalidInput = "\n{} [-] Invalid input".format(whiteSpace)

# Main
def main():
	print('\n')
	print'\t{}'.format(whiteSpace), decorator3
	print("{} Fybonacci: by Thabang".format(whiteSpace * 3))
	print'\t', decorator2
	print('\n')
	print("NOTE: Use Ctrl+C to quit the application.")
	prompt()

# Prompt the user to enter a number
def prompt():
	"""Prompt the user to enter a whole number."""
	try:
		number = int(raw_input('\n{} Enter a value: '.format(whiteSpace)))
		print("{0} Answer|Fib({1}) = {2}".format(whiteSpace, number, calculate(number)))
		prompt()
	
	except ValueError:
		print(invalidInput)
		prompt()
	
	except KeyboardInterrupt:
		print("\n\n{} Thank you for using Fybonacci Calculator! You're awesome!".format(whiteSpace))
		print('\n{0} >>> www.thabangsuccessor.blogspot.com'.format(whiteSpace))
		sys.exit()

# Calculate the Fibonacci value given by the user
def calculate(number):
	'''Return a list containing fibonacci
	series up to a value given by the user.'''
	a, b = 0, 1
	result = []
	if number == 0:
		return 0
	
	elif number == 1:
		return 0
	
	elif number < 0:
		result.append(b)
		a, b = b, a+b
		return result

	else:
		while b < number:
			result.append(a)
			a, b = b, a+b
		return result

# Do the math
main()

from math import pi



def area(r: int):
	""" 
	Program to compute the area of a circle upto 2 decimal places
	"""
	return round(pi * r**2, 2)

def circumference(r):
	""" 
	Program to computer the Circumference of a circle upto 2 decimal places
	"""
	return round(2 * pi * r, 2)

def is_even(n):
	"""
	Program to determine if a number is even or not.
	"""
	return n % 2 == 0

def is_vowel(c):
	"""
	Program to check if the given character is vowel or not
	"""
	all_vowels = 'aeiou'
	return c.lower() in all_vowels


def inches_to_cm(inch):
	"""
	Program to convert height from inches to centimeters
	"""
	return round(inch * 2.54, 2)



if __name__ == "__main__":
	pass
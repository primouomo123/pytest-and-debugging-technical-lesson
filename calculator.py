def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	if b == 0:
		raise ZeroDivisionError("Cannot divide by zero.")
	return a / b

if __name__ == "__main__":
	# Simple command-line interface
	print("Simple Calculator App")
	print(f"2 + 3 = {add(2, 3)}")
	print(f"10 - 5 = {subtract(10, 5)}")
	print(f"4 * 3 = {multiply(4, 3)}")
	print(f"8 / 2 = {divide(8, 2)}")

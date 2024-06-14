# Program to calculate the factorial of a number

# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Taking input from user
num = int(input("Enter a number: "))

# Checking if the number is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", num, "is", factorial(num))

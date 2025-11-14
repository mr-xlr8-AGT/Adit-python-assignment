# ASSIGNMENT 3 - Task 1: Calculate Factorial Using a Function
# Define a function to calculate factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number: "))

result = factorial(number)
print(f"Factorial of {number} is: {result}")

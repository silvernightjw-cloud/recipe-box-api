def add():
    # Function to add two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}")

def subtract():
    # Function to subtract two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 - num2
    print(f"The difference between {num1} and {num2} is {result}")

def multiply():
    # Function to multiply two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 * num2
    print(f"The product of {num1} and {num2} is {result}")

def divide():
    # Function to divide two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        return
    result = num1 / num2
    print(f"The quotient of {num1} and {num2} is {result}")

add()
subtract()
multiply()
divide()

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Cannot take square root of a negative number"
    return math.sqrt(a)

if __name__ == "__main__":
    print("Basic Calculator is ready!")

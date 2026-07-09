# Function
from py_compile import main


def add(*args):
    return sum(args)
def subtract(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
def divide(*args):
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ValueError("Cannot divide by zero")
        result /= num
    return result
def square(num):
    return num ** 2
def power(base, exponent):
    return base ** exponent
def square_root(num):
    if num < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return num ** 0.5

def calculate(operation, *args):
    if operation == 'add':
        return add(*args)
    elif operation == 'subtract':
        return subtract(*args)
    elif operation == 'multiply':
        return multiply(*args)
    elif operation == 'divide':
        return divide(*args)
    elif operation == 'square':
        if len(args) != 1:
            raise ValueError("Square operation requires exactly one argument")
        return square(args[0])
    elif operation == 'power':
        if len(args) != 2:
            raise ValueError("Power operation requires exactly two arguments")
        return power(args[0], args[1])
    elif operation == 'square_root':
        if len(args) != 1:
            raise ValueError("Square root operation requires exactly one argument")
        return square_root(args[0])
    else:
        raise ValueError("Invalid operation")
    
def main():
    print("Welcome to the calculator!")
    while True:
        operation = input("Enter operation (add, subtract, multiply, divide, square, power, square_root) or 'exit' to quit: ")
        if operation == 'exit':
            break
        args = input("Enter numbers separated by space: ").split()
        args = [float(arg) for arg in args]
        try:
            result = calculate(operation, *args)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
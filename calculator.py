def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: can't divide by zero")
        return None
    return a / b

def power(a, b):
    return a ** b

def calculator():
    print("=== CLI Calculator ===")
    print("Operations: add, subtract, multiply, divide, power")
    print("Type 'quit' to exit\n")

    while True:
        operation = input("Choose operation: ").strip().lower()

        if operation == "quit":
            print("Goodbye!")
            break

        if operation not in ["add", "subtract", "multiply", "divide", "power"]:
            print("Invalid operation, try again\n")
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if operation == "add":
            print(f"Result: {add(a, b)}\n")
        elif operation == "subtract":
            print(f"Result: {subtract(a, b)}\n")
        elif operation == "multiply":
            print(f"Result: {multiply(a, b)}\n")
        elif operation == "divide":
            result = divide(a, b)
            if result is not None:
                print(f"Result: {result}\n")
        elif operation == "power":
            print(f"Result: {power(a, b)}\n")

calculator()
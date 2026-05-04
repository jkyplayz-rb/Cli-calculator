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
    history = []
    print("=== CLI Calculator ===")
    print("Operations: add, subtract, multiply, divide, power, history")
    print("Type 'quit' to exit\n")

    while True:
        operation = input("Choose operation: ").strip().lower()

        if operation == "quit":
            print("Goodbye!")
            break

        if operation not in ["add", "subtract", "multiply", "divide", "power", "history"]:
            print("Invalid operation, try again\n")
            continue

        if operation == "history":
            if not history:
                print("No calculations yet\n")
            else:
                print("Last calculations:")
                for entry in history:
                    print(f"  {entry}")
                print()
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if operation == "add":
            result = add(a, b)
            print(f"Result: {result}\n")
            history.append(f"{a} + {b} = {result}")
        elif operation == "subtract":
            result = subtract(a, b)
            print(f"Result: {result}\n")
            history.append(f"{a} - {b} = {result}")
        elif operation == "multiply":
            result = multiply(a, b)
            print(f"Result: {result}\n")
            history.append(f"{a} * {b} = {result}")
        elif operation == "divide":
            result = divide(a, b)
            if result is not None:
                print(f"Result: {result}\n")
                history.append(f"{a} / {b} = {result}")
        elif operation == "power":
            result = power(a, b)
            print(f"Result: {result}\n")
            history.append(f"{a} ** {b} = {result}")

calculator()
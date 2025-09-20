# create calculator module in python to get user input and perform basic arithmetic operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def main():
    print("Simple Calculator")
    print("Enter two numbers:")
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
    except ValueError:
        print("Please enter valid numbers only.")
        return

    print("Select operation: add, subtract, multiply, divide")
    op = input("Operation: ").strip().lower()

    try:
        if op == "add":
            result = add(a, b)
        elif op == "subtract":
            result = subtract(a, b)
        elif op == "multiply":
            result = multiply(a, b)
        elif op == "divide":
            result = divide(a, b)
        else:
            print("Invalid operation.")
            return
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

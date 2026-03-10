def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


if __name__ == "__main__":
    print("Simple Calculator Test")

    print("Add:", add(5, 3))
    print("Subtract:", subtract(10, 4))
    print("Multiply:", multiply(6, 7))
    print("Divide:", divide(8, 2))

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("I'm being run directly", __name__)

if __name__ == '__main__':
    print(add(4, 3))
    print(subtract(4, 3))
    print(multiply(4, 3))
    print(divide(8, 4))

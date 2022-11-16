def greet(name):
    print(f"Hello!, {name}")

print(__name__)
if __name__  == "__main__":
    n = input("Enter the name\n")
    greet(n)
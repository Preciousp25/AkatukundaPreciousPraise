#positional arguments
def display(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

display("John", 20)

#keyword arguments
def display(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

display(name="John", age=20)
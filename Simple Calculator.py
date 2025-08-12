def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b
while True:
    print("##** Calculator **##")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = int(input("Enter your choice (1-5): "))
    
    if choice in {1,2,3,4}:
        a = input("Enter first number: ")
        b = input("Enter second number: ")
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
    if choice == 1:
            print(f"Result: {add(a, b)}")
    elif choice == 2:
            print(f"Result: {sub(a, b)}")
    elif choice == 3:
            print(f"Result: {mul(a, b)}")
    elif choice == 4:
            print(f"Result: {div(a, b)}")
    elif choice == 5:
            print("Exiting the calculator. Goodbye!")
            break
    else:
            print("Invalid choice. Please try again.")


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
    
import math_operations    

while True:
    print("\n---simple calculator---")
    print("1. add")
    print("2. substract")
    print("3. multiply")
    print("4. divide")
    print("5. Exit")

    choice = input("enter choice(1-5):")

    if choice == "5":
        print("goodbye.")
        break 
    
    elif choice in ("1","2","3","4"):
        try:
            num1 = float(input("enter the first number:"))
            num2 = float(input("entern the second number:"))
        except ValueError:
            print("invalid input. Please try again.")
            continue 
        
        if choice == "1":
            result = math_operations.add(num1, num2)
        elif choice == "2":
            result = math_operations.substract(num1, num2)
        elif choice == "3":
            result = math_operations.multiply(num1, num2)
        elif choice == "4":
            result = math_operations.divide(num1, num2)

        print(f"result: {result}")
    else:
        print("invalid choice, please try again")


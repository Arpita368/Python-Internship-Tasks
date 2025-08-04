def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    if b==0:
        return "Error: Division by zero is undefined"
    return a/b

while True:
    print("\nMENU \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5.Exit");
    choice = int(input("Enter your choice: "))
    if choice>0 and choice<5:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        if choice==1:
            print("Addition: ",add(a,b))
        elif choice==2:
            print("Subtraction: ",subtract(a,b))
        elif choice==3:
            print("Multiplication: ",multiply(a,b))
        elif choice==4:
            print("Divide: ",divide(a,b))
    elif choice==5:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Enter a valid number.")

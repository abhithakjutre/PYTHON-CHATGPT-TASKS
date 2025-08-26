# Task 3: Simple Calculator  
# Ask the user for two numbers and an operator (+, -, *, /) and perform the operation.


while True:
    num1 = int(input("\n\nEnter the first number : "))
    num2 = int(input("Enter the second number : "))
    print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1: 
        result = num1 + num2
        print(f"Your Result is : {result}")

    elif choice==2: 
        result = num1 - num2
        print(f"Your Result is : {result}")

    elif choice==3: 
        result = num1 * num2
        print(f"Your Result is : {result}")

    elif choice==4: 
        result = num1/num2
        print(f"Your Result is : {float(result)}")

    elif choice==5: 
        break
    else: 
        print("Invalid Choice :(")
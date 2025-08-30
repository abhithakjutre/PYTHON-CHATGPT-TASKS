'''Task 3: Check Armstrong Number  
An Armstrong number of 3 digits is a number such that:  
abc = a³ + b³ + c³  
Example: 153 = 1³ + 5³ + 3³  
- Ask user for a 3-digit number  
- Check if it's an Armstrong number'''



num1 = int(input("Enter 1 num: "))
num2= int(input("Enter 2 num: "))
num3 = int(input("Enter 3 num: "))

stringdigit = str(num1) + str(num2) + str(num3)


if num1**3 + num2**3 + num3**3 == int(stringdigit):
    print("It's Armstrong number")
else: 
    print("It's not an Armstrong number")
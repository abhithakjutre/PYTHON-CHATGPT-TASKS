# Task 1: Factorial using Loop  
# Ask the user for a number and print its factorial using a for loop.

num = int(input("Enter a number: "))
count = 1
for i in range(1,num+1): 
    count = count * i
print(f"factorial of {num} is: {count}")


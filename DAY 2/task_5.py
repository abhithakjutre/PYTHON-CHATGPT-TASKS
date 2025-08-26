# Task 5: Sum of N Numbers  
# Ask the user to enter a number n and print the sum of numbers from 1 to n.

number  = int(input("Enter a number: "))
sum = 0
for i in range(1,number+1):
    sum = sum + i
    
print(f"1 to {number} sum: {sum}")

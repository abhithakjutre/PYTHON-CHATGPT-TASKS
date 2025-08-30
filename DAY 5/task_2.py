'''Task 2: Find Second Largest Number in a List  
Ask the user to enter 6 numbers.  
Store them in a list and print the second largest number.'''



list = []

for i in range(1,7): 
    num = int(input(f"Enter {i} number: "))
    list.append(num)


first_largest = max(list)
list.remove(first_largest)
print(f"Second largest number is: {max(list)}")
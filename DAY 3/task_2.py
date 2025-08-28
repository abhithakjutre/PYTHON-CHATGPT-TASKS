# Task 2: Reverse a Number  
# Take a number from the user and print it in reverse. (e.g. input: 123 → output: 321)

num = int(input("Enter a number: "))
reverse = str(num)[::-1]
print(f"Reverse number is : {int(reverse)}")

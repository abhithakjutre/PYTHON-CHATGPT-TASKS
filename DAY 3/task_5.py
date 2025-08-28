# Task 5: Fibonacci Series  
# Ask the user for a number n and print the first n numbers of the Fibonacci series.


num = int(input("Enter a number: "))
a = 0
b = 1
for i in range(num):
    print(f" {a} " , end="")
    temp = a
    a = b
    b = temp + b

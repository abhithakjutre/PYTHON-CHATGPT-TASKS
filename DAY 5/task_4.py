'''Task 4: Function to Find Factorial (Using Function)  
Write a function factorial(n) that returns the factorial of a number.
'''


def factorial(n): 
    if n == 0 or n == 1:
        return 1
    else: 
        return n * factorial(n-1)
    

print(factorial(5))
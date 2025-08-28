'''
Task 5: Prime Number Checker
- What to do:
  - Ask the user to enter a number.
  - Check if it’s a prime number (only divisible by 1 and itself).'''


num = int(input("Enter a number: "))

if num<=1:
    print(num," It's not prime number")

else: 
    is_prime = True
    for i in range(2,int(num**0.5)+1):
        if num%i==0: 
            is_prime = False
            break
        
    if is_prime == True: 
        print(num," It's prime number")

    else: 
        print(num," It's not prime number")
            


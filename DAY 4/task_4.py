'''Task 4: Function to Add Two Numbers
- What to do:
  - Define a function called add(a, b) that returns a + b.
  - Ask the user to enter two numbers.
  - Call the function using those numbers and print the result.
'''

def add(a,b): 
    return a + b



num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2st number: "))
print(f"Result : {add(num1,num2)}")
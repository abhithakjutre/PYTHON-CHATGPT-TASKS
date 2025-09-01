'''🔹 Task 2: Find All Prime Numbers up to N
- User se ek number N lo  
- 1 se N tak saare prime numbers print karo  
- Hint: Use for loop + nested loop ya ek is_prime(n) function bana sakte ho
'''

num = int(input("Enter a number: "))

for i in range(1,num+1): 
    if i>1: 
        for j in range(2,i): 
            if i%j==0: 
                break
        else: 
            print(i, end=" ")
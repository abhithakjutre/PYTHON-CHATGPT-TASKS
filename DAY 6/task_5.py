'''🔹 Task 5: Check Perfect Number
- Perfect number wo hota hai jiska sum of divisors (excluding itself) = number
  - Example: 6 → 1+2+3 = 6
- User se number lo, check karo kya wo perfect number hai.
'''

divisor = 0
num = int(input("Enter a number: "))
for i in range(1,num):
    if num%i==0:
        divisor+=i
        print(divisor)

if divisor==num:
    print("It's  Perfect number : ",num)

else:
    print("It's not Perfect number")
'''
🔹 Task 1: Count Positive, Negative, and Zero
- User se 10 numbers lo (loop se).
- Count karo kitne numbers:
  - Positive hain
  - Negative hain
  - Zero hain
'''

positive_number = 0
negative_number = 0
zero = 0

for i in range(1,11):
    num = int(input(f"Enter {i} number: "))
    if num>0:
        positive_number+=1
    elif num<0:
        negative_number+=1
    else:
        zero+=1

print("Positive number : ",positive_number)
print("Negative number : ",negative_number)
print("Zero : ",zero)
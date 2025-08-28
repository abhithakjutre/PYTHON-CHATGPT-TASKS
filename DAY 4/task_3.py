'''
Task 3: Find Duplicates in a List
- What to do:
  - Ask the user to enter 6 numbers, one by one.
  - Store all 6 numbers in a list.
  - Check and print any numbers that are repeated (duplicates).
  - Example: if user enters [2, 4, 3, 2, 6, 3], output should be 2 and 3.

'''


l = []

for i in range(1,7): 
    num = int(input(f"Enter {i} number: "))
    l.append(num)

duplicate = []

for num in l: 
    if l.count(num) > 1 and num not in duplicate: 
        duplicate.append(num)

for item in duplicate: 
    print(f"Dupilcate value : {item}")
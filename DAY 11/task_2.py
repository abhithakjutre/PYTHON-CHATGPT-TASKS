'''🔹 Task 2: Create Dictionary of Squares
- Ask the user to enter 5 numbers.
- Create a dictionary where:
  - Key = number
  - Value = square of the number
- Example: {2: 4, 3: 9, ...}
'''

result_dict = {}

for item in range(1,6): 
    num = int(input(f"Enter {item} number: "))
    result_dict[num] = num*num

print(result_dict)
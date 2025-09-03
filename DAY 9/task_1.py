'''🔹 *Task 1: Multiply All Items in a List*
- User se 5 numbers lo.
- List me store karo.
- Saare numbers ko multiply karke final product print karo.
'''

num_list = []

for i in range(1,6):
    numbers = int(input(f"Enter {i} number: "))
    num_list.append(numbers)


result = 1

for j in range(1,6): 
    for item in range(0,5): 
     result+=num_list[item]*num_list[j+1]



print(result)
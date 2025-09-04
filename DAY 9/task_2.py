'''🔹 *Task 2: Find the Second Smallest Number*
- 6 numbers lo user se.
- List me store karo.
- Second smallest number print karo (without using `sort()`).
'''

num_list= []

for i in range(1,7):
    num = int(input(f"Enter {i} number: "))
    num_list.append(num)

small_num = min(num_list[0],num_list[1])
second_small_num = max(num_list[0],num_list[1])

for item in num_list[2:]: 
    if item<small_num: 
        second_small_num = small_num
        small_num = item
    elif small_num<item<second_small_num: 
        second_small_num = item
    
print(f"Second smallest number : {second_small_num}")
    
'''🔹 Task 4: Find Common Elements Between Two Lists
- User se do lists lo (5-5 numbers)  
- Print karo common elements jo dono lists me hain  
- Bonus: Use sets for faster lookup'''

list1 = set()
list2 = set()

for i in range(1,3): 
    for j in range(1,6): 
        list_elements = int(input(f"Enter {j}th element of list {i}: "))
        if i == 1:
            list1.add(list_elements)
        if i == 2: 
            list2.add(list_elements)


result = set(list1.intersection(list2))
print(result)
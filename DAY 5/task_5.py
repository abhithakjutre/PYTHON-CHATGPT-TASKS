'''
Task 5: Create a List from User and Reverse It  
- Ask user to enter 5 numbers  
- Store in a list  
- Print original and reversed list (without using reverse() or slicing)'''


list = []
for i in range(1,6): 
    num = int(input(f"Enter {i} number: "))
    list.append(num)

reversed_list = []
print(f"Original list: {list}")
for i in range(len(list)-1,-1,-1): 
    reversed_list.append(list[i])

print(f"Reversed list: {reversed_list}")
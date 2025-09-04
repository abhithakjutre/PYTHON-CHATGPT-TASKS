'''🔹 *Task 4: Create Dictionary from 2 Lists*
- List1: Names → `["Ram", "Shyam", "Geeta"]`
- List2: Marks → `[85, 90, 78]`
- Ek dictionary banao jisme name = key, marks = value
'''

list1 = ["Ram", "Shyam", "Geeta"]
list2 = [85, 90, 78]
list_dict = {}

list_len = len(list1)


for i in range(0,3): 

    list_dict[list1[i]]=  list2[i]

print(list_dict)
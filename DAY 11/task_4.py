'''🔹 Task 4: Find Common Letters Between Two Strings
- Ask the user to enter two strings.
- Print the common letters (ignore duplicates, case-insensitive).
- Example: "hello" and "world" → Output: ['l', 'o']
'''




string1 = input("Enter a first string : ")
string2 = input("Enter a second  string : ")
set_1 = {char for char in string1.lower()}
set_2 = {char for char in string2.lower()}
result_set = set_1.intersection(set_2)

print(f"Output : {list(result_set)}")
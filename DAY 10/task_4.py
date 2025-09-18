'''🔹 Task 4: Merge Two Lists into a Dictionary
- Take 2 user inputs:
  - 3 keys → e.g., ["name", "age", "city"]
  - 3 values → e.g., ["Amit", 22, "Delhi"]
- Create a dictionary by merging them.
- Print the dictionary.
'''


list_1 = ["name", "age", "city"]
list_2 = ["Amit", 22, "Delhi"]
result_dict = {
}
for i in range(3):
    result_dict[list_1[i]] = list_2[i]

print(result_dict)
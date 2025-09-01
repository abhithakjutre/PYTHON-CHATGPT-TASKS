'''🔹 Task 3: Count Frequency of Each Character in a String
- User se ek string lo  
- Har character kitni baar aaya hai, wo count karo  
- Output should be like:
  
  h → 1  
  e → 2  
  l → 3  
  o → 1
  '''




user_str = input("Enter a string: ")

str_dict = {}
for i in user_str: 
    if i in str_dict:
        str_dict[i] += 1
    else: 
        str_dict[i] = 1

for i, count in str_dict.items(): 
    print(f"{i} -> {count}")

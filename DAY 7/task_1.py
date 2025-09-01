'''🔹 Task 1: Remove Vowels from a String
- User se ek string lo  
- Us string se saare vowels (a, e, i, o, u) hata do  
- Output me vowel-removed string print karo  
- Example: "hello world" → "hll wrld"'''



user_str = input("Enter a string: ")

vowels = "a,e,i,o,u,A,E,I,O,U"

final_str = [i for i in user_str if i not in vowels]

print("String after removing vowels: ",end="")

for item in final_str: 
    print(item, end="")


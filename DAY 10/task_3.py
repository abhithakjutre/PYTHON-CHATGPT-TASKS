'''🔹 *Task 3: Replace Vowels with '*'*
- Ask user to enter a string.
- Replace all vowels (a, e, i, o, u) with `*`.
- Example: `"hello"` → `"h*ll*"`
'''

vowels ='aeiou'

user_str = input("Enter a string: ")
result = ""
for char in user_str: 
    if char in vowels: 
           result+="*"
    else: 
        result += char

print(result)
          
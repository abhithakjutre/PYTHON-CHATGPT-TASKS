
# Task 3: Count Vowels in a String  
# Ask the user to enter a string and count how many vowels (a, e, i, o, u) it has.

string = input("Enter a string: ")
s = string.lower()

vowels = "aeiou"
count = 0 
for char in s: 
    if char in vowels:
        count = count+ 1 

print(f"Vowels in string: {count}")
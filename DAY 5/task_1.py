'''Task 1: Count Digits, Alphabets, and Special Characters  
Ask the user to enter a string. Count:
- Number of alphabets (a–z, A–Z)
- Number of digits (0–9)
- Number of special characters (anything else)'''



text = input("Enter a string: ")


aphabet_count = 0
digit = 0
special_char = 0

for char in text: 
    if char.isalpha(): 
        aphabet_count +=1
    elif char.isdigit():
        digit +=1
    else: 
        special_char +=1

print(f"Number of alphabets: {aphabet_count}")
print(f"Number of digits: {digit}")
print(f"Number of special characters: {special_char}")


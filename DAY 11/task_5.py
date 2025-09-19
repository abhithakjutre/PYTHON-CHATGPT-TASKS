'''
🔹 Task 5: Function to Count Consonants
- Create a function count_consonants(s)
- It should return the number of consonants in the string (not vowels or digits).
- Ignore spaces and special characters.
'''



def count_consonants(s): 
    consonants = "bcdfghjklmnpqrstvwxyz"
    consonants_counts = 0
    for item in s: 
        if item in consonants: 
            consonants_counts+=1
        else: 
            continue
    return consonants_counts


user_str = input("Enter a string: ")

print(f" Consonants: {count_consonants(user_str)}")
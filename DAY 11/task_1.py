'''🔹 Task 1: Count Words Ending with a Vowel
- Ask the user for a sentence.
- Count how many words end with a vowel (a, e, i, o, u).
- Example: "He is a true hero" → 2 (words: "a", "hero",etc.)
'''

user_sentence = input("Enter a sentence: ")
vowels = "aeiou"
count = 0
vowels_word = []
for word in user_sentence.split(): 
    if word[-1] in vowels: 
        count += 1
        vowels_word.append(word)
    else: 
        continue

print(f"{count} words ( ", end="")

for item in vowels_word: 
    print(f'''"{item}",''', end=" ")

print(" )")



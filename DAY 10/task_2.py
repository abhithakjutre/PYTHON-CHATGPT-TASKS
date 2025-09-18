'''
🔹 *Task 2: Sort Words Alphabetically*
- Ask the user to enter a sentence.
- Split into words.
- Sort the words in *alphabetical order*.
- Print sorted words line by line.'''

sentence  = input("Enter a sentence: ")

words = sentence.split()

words.sort()

for word in words: 
    print(word)
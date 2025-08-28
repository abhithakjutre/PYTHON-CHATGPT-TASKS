'''Task 2: Count Words in a Sentence
- What to do:
  - Ask the user to enter a sentence (e.g., “Python is fun”).
  - Count how many words are in the sentence.
  - Hint: You can split the sentence using split() and count the list length.
'''


sentence = input("Enter a sentence: ")

result = sentence.split()
print(f"your words in sentence:  {len(result)}")

'''🔹 Task 3: Find Largest Word in a Sentence
- User se sentence lo.
- Print karo sabse lamba word (largest length).'''

user_sentence = input("Enter a Sentence: ")


max_word = ""
for word in user_sentence.split():
    if len(word) > len(max_word):
        max_word = word

print(f"Largest Word is : {max_word}")


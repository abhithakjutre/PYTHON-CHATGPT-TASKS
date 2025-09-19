'''🔹 Task 3: Find Longest Word
- Ask the user to enter a sentence.
- Find and print the longest word in the sentence along with its length.
- Example: "Python is amazing" → Longest: "amazing" (7 letters)
'''

user_sentence = input("Enter a sentence: ")
result_dict = {}
values_list = []

for word in user_sentence.split(): 
    result_dict[len(word)] = word
    values_list.append(len(word))


print(f''' Longest: "{result_dict[max(values_list)]}" ({max(values_list)} letters) ''')
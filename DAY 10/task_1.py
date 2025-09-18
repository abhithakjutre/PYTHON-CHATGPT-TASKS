'''
🔹 *Task 1: Check Pangram*
- A pangram contains *all 26 letters* of the alphabet.
- Example: `"The quick brown fox jumps over the lazy dog"` ✅
- *Input*: Ask user for a sentence.
- *Output*: Print whether it's a pangram or not.'''

sentence = input("Enter a sentence: ")

a_to_z = "abcdefghijklmnopqrstuvwxyz"

if all(char in sentence for char in a_to_z):
    print("Pangram")
else:
    print("Not Pangram")



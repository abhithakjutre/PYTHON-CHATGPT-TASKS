'''Task 1: Palindrome Checker
- A palindrome is a word that reads the same forward and backward.
- Example: "madam", "level", "121"
- What to do:
  - Ask the user to enter a string.
  - Check if the string is equal to its reverse.
  - If yes, print "It is a palindrome", else print "Not a palindrome".'''

string = input("Enter a string: ")

result = str(string[::-1])

if string==result: 
    print("It is a palindrome.")

else: 
    print("It is not palindrome.")


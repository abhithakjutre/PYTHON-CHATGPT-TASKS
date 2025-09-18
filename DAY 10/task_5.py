'''🔹 Task 5: Function to Count Uppercase, Lowercase, and Digits
- Function: analyze_string(s)
- Ask user for a string.
- Count:
  - Uppercase letters
  - Lowercase letters
  - Digits
- Print the counts.
'''


def analyze_string(s):
    count_digit = 0
    count_upper = 0
    count_lower = 0

    for item in s:
            if item.isdigit():
                count_digit += 1
            elif item.isupper():
                count_upper +=1
            elif item.islower():
                count_lower +=1
            elif item == " ":
                continue
    print(f"Digits: {count_digit}\nUppercase Letters: {count_upper}\nLowercase Letters:{count_lower}")


user_string = input("Enter a string: ")
analyze_string(user_string)
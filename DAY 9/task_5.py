'''🔹 *Task 5: Password Strength Checker*
- User se password input lo.
- Check karo:
  - At least 8 characters
  - Contains letter, digit, and special character
- Output: Strong / Weak'''

usr_psw = input("Enter Your Password: ")

if len(usr_psw)>=8:
    if any(ch.isalpha() for ch in usr_psw) and any(ch.isdigit() for ch in usr_psw) and any(ch.isalnum for ch in usr_psw):

        print("Strong Password")
    else: 
        print("Weak Password")
else: 
    print("At least 8 characters")
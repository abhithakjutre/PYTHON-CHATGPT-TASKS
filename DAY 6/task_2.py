'''🔹 Task 2: Check Leap Year
- User se ek year lo.
- Check karo kya wo leap year hai ya nahi.
  - Leap year rule: divisible by 4, but not by 100 unless also divisible by 400.'''

user_year = int(input("Enter a year: "))

if user_year%400==0:
    print(f" {user_year} is Leap Year. ✅")
elif user_year%100==0:
    print(f" {user_year} is  Not Leap Year. ❌ ")
elif user_year%4==0:
    print(f" {user_year} is Leap Year. ✅")
else:
    print(f" {user_year} is  Not Leap Year. ❌ ")



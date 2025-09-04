'''🔹 *Task 3: Function to Check Armstrong Number (Generalized)*
- Function `is_armstrong(n)` banao.
- Wo check karein kya number Armstrong hai (chahe 3-digit ho ya 4-digit).
  - Example: 9474 → 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474 ✅
'''


def is_armstrong(n):
    str_num = str(n)
    len_str = len(str_num)
    result = 0
    for digit in str_num: 
        result+= int(digit)**len_str

    if result == n: 
        print(f"{n} is Armstrong Number ")
    else: 
        print(f"{n} is not Armstrong Number")


number = int(input("Enter number: "))

is_armstrong(number)



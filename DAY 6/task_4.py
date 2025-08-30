'''🔹 Task 4: Sum of Digits (Using Function)
- Function banao sum_digits(n)
- User se number lo, aur function ka use karke uske sab digits ka sum nikalo
  - Example: 123 → 1+2+3 = 6'''


def sum_digits(n):
    digit_ls = []
    result = 0
    string_n = str(n)
    for item in string_n:
        digit_ls.append(int(item))
    for i in digit_ls:
        result+=i
    return result


num = int(input("Enter a number: "))
print(f"Sum of Digits is :{sum_digits(num)}")
'''🔹 Task 5: Function to Check Palindrome Number
- Function banao is_palindrome(n)  
- Number ko string me convert karke check karo kya wo reverse ke equal hai  
- Input: 121 → Palindrome  
- Input: 123 → Not Palindrome
'''

def is_palindrome(n): 
    num_str = str(n)
    if num_str == num_str[::-1]:
        return "Palindrome"
    else: 
        return "Not Palindrome"
    
result = is_palindrome(121)
print(result)

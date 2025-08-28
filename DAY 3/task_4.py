# Task 4: List Operations  
# Ask the user to enter 5 numbers (use a loop), store them in a list, and then:
# - Print the list
# - Print the maximum and minimum value

l = []

for i in range(1, 6): 
    value = int(input(f"Enter {i} number: "))
    l.append(value)
 
print(f"list : {l}")
print(f"maximum value: {max(l)}")
print(f"minimum value: {min(l)}")

   
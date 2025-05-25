# Short-Hand If and If-Else (Ternary Operators)
# Ternary if-else:
'''
Syntax of the Ternary Operator:

value_if_true if condition else value_if_false

'''

# Example 1:
status = "Eligible" if age >= 18 else "Not Eligible"

x = 10
if x > 5: print("Greater than 5")  # One-line if


# Example 2:
x = 5
y = "High" if x > 10 else "Low"
print(y)  # Output: Low


# Example 3: Inside a print statement:
number = 5
print(f"{number} is {'Even' if number % 2 == 0 else 'Odd'}")


#Example 4: Return value from a function:
def max_of_two(a, b):
    return a if a > b else b


# Example 5: Determining a User's Access Level
is_admin = True
access_level = "Full Access" if is_admin else "Limited Access"
print(f"User access: {access_level}")
# Output: User access: Full Access


# Example 6: Checking if a Number is Positive or Non-Positive
num = -7
sign = "Positive" if num > 0 else "Non-Positive"
print(f"The number is: {sign}")
# Output: The number is: Non-Positive

# Example 7: 
# Traditional
x = 10
if x > 5: print("x is greater than 5")

# Single-line 'if' (sometimes called short-hand if)
y = 3
if y > 5: print("y is greater than 5") # This line won't print

# Output: x is greater than 5
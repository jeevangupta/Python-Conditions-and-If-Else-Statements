
'''
Syntax of if Statement

if condition:
    # code block to execute if condition is True
    # This block of code must be indented

'''
#Simple Examples of if in Action


#Example 1: Checking a number
num = 10
if num > 0:
    print("\n Positive number")

#Output: Positive number



#Example 2: Comparing strings
language = "Python"
if language == "Python":
    print("\n You are learning Python!")

#Output: You are learning Python!


#Example 3: Using a boolean value
is_logged_in = True
if is_logged_in:
    print("\n Welcome back!")

#Output: Welcome back!



# Example 4: Determining if a number is even
my_number = 14

# The modulo operator (%) returns the remainder of a division
# If a number divided by 2 has a remainder of 0, it's even.
if my_number % 2 == 0:
    print(f"\n {my_number} is an even number.")

my_number = 7
if my_number % 2 == 0:
    print(f"\n {my_number} is an even number.") # This won't print

#Output: 14 is an even number.

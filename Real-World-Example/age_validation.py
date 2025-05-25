# python3 age_validation.py
'''
Scenario: Asking a user for their age and ensuring it's a valid number.
'''

'''
Explanation:

The outer if checks if the input is purely numeric using isdigit().
If it is, the code enters that block, converts the string to an integer, 
and then an inner if-else checks if the age falls within a plausible range (0-120).
If isdigit() is False, the outer else block handles the non-numeric input error.
'''

user_input_age = input("Please enter your age: ")

if user_input_age.isdigit(): # Check if the input consists only of digits
    age = int(user_input_age) # Convert to integer
    if age >= 0 and age <= 120: # Check for a reasonable age range
        print(f"Thank you. Your age is: {age}")
    else:
        print("Error: Age must be between 0 and 120 years.")
else:
    print("Error: Invalid input. Please enter a numerical value for age.")
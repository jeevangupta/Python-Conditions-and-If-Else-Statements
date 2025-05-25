# If-Else with Logical Operators (and, or, not)

# The and Operator: Requiring Multiple Truths
age = 20
country = "India"
if age >= 18 and country == "India":
    print("Eligible to vote")
else:
    print("Not eligible")



# The or Operator: Satisfying at Least One Condition
role = "admin"
if role == "admin" or role == "moderator":
    print("Access granted")
else:
    print("Access denied")



# The not Operator: Negating a Condition
is_logged_in = True
if not is_logged_in:
    print("Please log in to continue")


# Example 1: Using and and or:
user = "admin"
is_active = True
if (user == "admin" or user == "editor") and is_active:
    print("Welcome to the dashboard")
else:
    print("Access denied")

# Example 2: Using not with and:
has_permission = False
if not (age < 18 and has_permission == False):
    print("Allowed")
else:
    print("Not allowed") 


# Example 3: Complex Admission Criteria
has_high_school_diploma = True
gpa = 3.8
sat_score = 1250
is_athlete = False

# Admission criteria:
# (High school diploma AND (GPA > 3.5 OR SAT score > 1200)) OR is_athlete
if (has_high_school_diploma and (gpa > 3.5 or sat_score > 1200)) or is_athlete:
    print("Congratulations! You are admitted.")
else:
    print("Admission criteria not met.")

'''
Output -> Congratulations! You are admitted.
'''


# Example 5: Validating User Input for a Password
password = "Pass123!"

# Password must be at least 8 characters long, AND
# contain at least one digit, AND
# contain at least one special character (for simplicity, using '!' or '@')
if len(password) >= 8 and any(char.isdigit() for char in password) and ('!' in password or '@' in password):
    print("Password is strong.")
else:
    print("Password is weak. Please meet the criteria.")

'''
Output -> Password is strong.
'''


# Example 6: Checking if a List is Not Empty
my_list = []

if not my_list: # An empty list is considered 'Falsy', so 'not' makes it True
    print("The list is empty.")
else:
    print("The list contains items.")

my_list = [1, 2, 3]
if not my_list: # A non-empty list is 'Truthy', so 'not' makes it False
    print("The list is empty.")
else:
    print("The list contains items.")

'''
The list is empty.
The list contains items.
'''
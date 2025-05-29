
# Consider this example where the order is slightly off:
age = 25
#
# Incorrect order for a typical age categorization
if age >= 18:
    print("Eligible to vote.")
elif age >= 21: # This condition will never be reached if age is >= 21 and also >= 18
    print("Eligible to drink.")
else:
    print("Too young.")

# Output (for age = 25) -> Eligible to vote.

'''
Problem: Even though age = 25 is eligible to drink, the program only prints "Eligible to vote." 
This is because age >= 18 is True for 25, so that block executes, and the elif age >= 21 condition 
is never even checked.
'''


#
# Corrected Order:
age = 25

# Correct order for typical age categorization (most specific to least specific)
if age >= 21:
    print("Eligible to drink and vote.")
elif age >= 18: # This is only checked if age < 21
    print("Eligible to vote.")
else:
    print("Too young.")

# Output (for age = 25): Eligible to drink and vote.

'''
Explanation: By placing the more specific condition (age >= 21) first, we ensure it's 
evaluated before the broader condition (age >= 18). This ensures the correct and most specific 
outcome is achieved.
'''
#
# Example 1: Checking Pass or Fail
score = 75

if score >= 60:
    print("Congratulations! You passed the exam.")
else:
    print("Sorry, you did not pass. Please try again.")

print("End of grading process.")

'''
Output (for score = 75):
Congratulations! You passed the exam.
End of grading process.


Output (for score = 45):
Sorry, you did not pass. Please try again.
End of grading process.
'''


# Example 2: Even or Odd Number
number = 9

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

'''
9 is an odd number.
'''

# Example 3: A Simple Grading System
student_score = 88

if student_score >= 90:
    print("Grade: A")
elif student_score >= 80: # This only runs if score < 90
    print("Grade: B")
elif student_score >= 70: # This only runs if score < 80
    print("Grade: C")
elif student_score >= 60: # This only runs if score < 70
    print("Grade: D")
else: # This only runs if score < 60
    print("Grade: F")

print("Grading complete.")

'''
Output (for student_score = 88):

Grade: B
Grading complete.
'''
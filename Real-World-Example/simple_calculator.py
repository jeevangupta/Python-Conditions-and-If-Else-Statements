# python3 simple_calculator.py
'''
Scenario: A simple calculator that performs addition, subtraction, or exits.
'''
'''
Each elif condition corresponds to a different menu option. 
Only the block associated with the user's valid choice will execute. 
The else block catches any invalid input.
'''

print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Exit")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {num1 + num2}")
elif choice == '2':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"Result: {num1 - num2}")
elif choice == '3':
    print("Exiting calculator. Goodbye!")
else:
    print("Invalid choice. Please select 1, 2, or 3.")
# python3 weather_categorizer.py
'''
Scenario: Categorizing temperatures as 'Freezing', 'Cold', 'Moderate', or 'Hot'.
'''
'''
Explanation:
This if-elif-else chain efficiently categorizes a numerical value into distinct ranges, 
a common task in data processing. Notice how the elif conditions implicitly leverage the 
fact that previous conditions were False (e.g., the second elif only runs if temp > 0 
because if temp <= 0 was True, the first if would have executed).
'''

current_temp_celsius = 28.5

if current_temp_celsius <= 0:
    print("Weather: Freezing!")
elif current_temp_celsius > 0 and current_temp_celsius <= 10:
    print("Weather: Cold.")
elif current_temp_celsius > 10 and current_temp_celsius <= 25:
    print("Weather: Moderate.")
else: # current_temp_celsius > 25
    print("Weather: Hot!")
# game_adventure.py
'''
Scenario: A simplified text-based adventure game decision.
'''
'''
Explanation:
Complex conditions using and and or determine the outcome.
Different actions and health penalties are applied based on the combination of 
player_health and player_weapon.
The else provides a general fallback if none of the specific fighting conditions are met.
'''

player_health = 80
enemy_power = 60
player_weapon = "sword" # Could be "bow", "fist", etc.

print("You encounter a fearsome goblin!")

if player_weapon == "sword" and player_health > 50:
    print("You bravely charge with your sword and defeat the goblin!")
    player_health -= 10 # Minor health loss
elif player_weapon == "bow" and player_health > 30:
    print("You cunningly use your bow to strike the goblin from a distance!")
    player_health -= 5
elif player_health <= 50 and player_weapon == "fist":
    print("You try to fight with your fists, but the goblin is too strong. You flee!")
    player_health -= 20 # Significant health loss for fleeing unprepared
else:
    print("You are too weak or unprepared. You retreat and live to fight another day.")
    player_health -= 5

print(f"Your remaining health: {player_health}")
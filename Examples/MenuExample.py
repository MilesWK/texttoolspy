"""
MenuExample.py

This program will demonstrate how to use the menu() function in the 
texttoolspy module. 

Read the docs here: https://github.com/MilesWK/texttoolspy/
"""


import texttoolspy as ttp # Import our module

Items = ["Left","Right","Up","Down"] # The array of objects that will serve as the menu options

user_input = ttp.menu(Items, 1) # Get the returned item from our menu() function. The "1" is the type of menu

print(f"The user chose to go {user_input}.") # Print the item the user chose

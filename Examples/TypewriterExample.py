"""
TypewriterExample.py
This program will demonstrate how to use the typewriter() function in the 
texttoolspy module. 
Read the docs here: https://github.com/MilesWK/texttoolspy/
"""
#-------------------------------------------------------#
# This program will type out whatever the user inputted #
#-------------------------------------------------------#
import texttoolspy as ttp # Import our module

# Get what we want our "typer" to type out
user_input = input("Enter something that will be typed out: ")

# Type out the user input
ttp.typewriter(user_input)


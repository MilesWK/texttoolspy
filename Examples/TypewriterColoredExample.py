"""
TypewriterColoredExample.py
This program will demonstrate how to use the typewriterColored() function in the 
texttoolspy module. 
Read the docs here: https://github.com/MilesWK/texttoolspy/
"""


import texttoolspy as ttp # Import our module

# The colors that can be used to print stuff out with the function
colors = ["red","yellow","green","cyan","blue","magenta"]
# Get the user input
user_input = input("Enter something you want typed out: ")

for item in colors: # repeat this for each item that is in our "colors" array
  ttp.typewriterColored(user_input, item)

"""
TypewriterColoredExample.py
This program will demonstrate how to use the typewriterColored() function and typewriter() can be used together in the 
texttoolspy module. 
Read the docs here: https://github.com/MilesWK/texttoolspy/
"""

import texttoolspy as ttp # Import our module


# First line of text

ttp.typewriter("Hello! Welcome! This is another demo of how the ", 5, False)
ttp.typewriterColored("typewriter() ", "red", 5, False)
ttp.typewriter("function and the ", 5, False)
ttp.typewriterColored("typewriterColored() ", "red", 5, False)
ttp.typewriter("function can be used together in harmony! \n ", 5, True)

# Second line of text

ttp.typewriter("Since all the typing functions aside from the last one per line has linebreak set to ", 5, False)
ttp.typewriterColored("False", "red", 5, False)
ttp.typewriter(", this allows colors to be added in lines, allowing for a ", 5, False)
ttp.typewriterColored("seamless ", "red", 5, False)
ttp.typewriter("transition! \n ", 5, True)

# Third line of text

ttp.typewriter("Is this cool? If so, check out the ", 5, False)
ttp.typewriterColored("Github repository ", "red", 5, False)
ttp.typewriter("for how to use this! Here is the link: \n \n", 5, False)
ttp.typewriterColored("https://github.com/MilesWK/texttoolspy/ \n\n", "red", 5, False)
ttp.typewriter("I hope you have fun! \n ", 5, True)

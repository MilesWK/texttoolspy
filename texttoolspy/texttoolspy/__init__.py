from termcolor import colored
import colorama
from sys import stdout
from time import sleep
from readchar import key, readkey
import os
import cursor
colorama.init()
bold = '\033[1m'
italic = '\x1B[3m'

def write(letter, speed):
  stdout.write(letter)
  stdout.flush()
  if letter != " ":
    sleep(0.01 * speed)
  
def typewriter(string=None, speed=5, LineBreak=True):
  cursor.hide()
  if string == None:
    print("TypeError: missing 'string'")
  else:
    for x in range(0,len(string)):
      write(string[x], speed)
    if LineBreak == True:
      print("  ")
    cursor.show()
def typewriterColored(string=None, color="white", speed=5, LineBreak = True):
  cursor.hide()
  if string == None:
    print("TypeError: missing 'string'")
  try:
    for x in range(0, len(string)):
      write(colored(string[x], color.lower()), speed)
    if LineBreak == True:
      print("  ")
  except Exception as e:
    if color.lower() in str(e):
      print("  ")
      print(colored("'"+color.lower()+"'" + " is not a registerd color. Please see the github documentation for the full list of registerd colors","red"))
    elif "missing" in str(e):
      print(str(e) + "-> No string was given.")
  cursor.show()
def LineBreak(lines):
  for x in range(0,lines):
    print("  ")
def menu(menu_items,menu_type):
  selected_menu = 1
  answer = ""
  while answer != key.ENTER:
    os.system("cls")
    for x in range(0,len(menu_items)):
      if selected_menu == x+1:
        if str(menu_type)=="1":
          print(f"> {italic}{menu_items[x]} \n")
        elif str(menu_type)=="2":
          print(colored(f"{bold}{menu_items[x]} \n","black","on_white"))
        elif str(menu_type) == "3":
          print(colored(f"{menu_items[x]} \n","red"))
      else:
        print(menu_items[x] + "\n")
    sleep(0.1)
    answer = readkey()
    if answer == key.DOWN and selected_menu < len(menu_items):
      selected_menu += 1
    elif answer == key.UP and selected_menu > 1:
      selected_menu -= 1
  
  Selected = menu_items[selected_menu-1]
  return Selected
  os.system("cls")
  
  

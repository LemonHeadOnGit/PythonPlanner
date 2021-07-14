r"""
   PythonPlanner | v0.2.0_b3 
   - This software is currently in HEAVY development. There are no actual functions implemented yet.
   - Use this software at your own risk. (Also, any meaningful contributions are appreciated!) 
"""

#   /// IMPORT MODULES

import os
import datetime
import time
import linecache

#   /// CREATE VARIABLES NEEDED

nogui = True
f = os.path.isfile
rm = os.remove
fExist = True
TP = "T"
TiPl = "TIMETABLE"
choice = 0
if os.name == 'nt':
    clr = 'cls'
else: clr = 'clear'

#   /// WRITE TO (OR CREATE) CONFIG FILE

if f("config.txt") == True:
    open("config.txt", "r")
else:
    print("No config file detected, creating...\n\n\n")
    config = open("config.txt", "w+")
    fExist = False

#   /// PROCEED WITH PLANNER SETUP (IF ABOVE CHECK RETURNS FALSE)

if fExist == False:
    cfgpar = input("Would you like the CLI [C] or (INDEV) GUI [G] view?\n=====\nCHOICE: ")
    print("=====\n")
    if cfgpar.capitalize() not in ["C","G"]:
        print("Invalid choice, defaulting to CLI.")
        cfgpar = "C"
    config.writelines(cfgpar+"\n")
    
    cfgpar = input("Would you like Timetable [T] or Planner [P] mode?\n=====\nCHOICE: ")
    print("=====\n")
    if cfgpar.capitalize() not in ["T","P"]:
        print("Invalid choice, defaulting to Planner.")
        cfgpar = "P"
    config.writelines(cfgpar)
    TP = cfgpar
    
    config.close()

#   /// DO SOME THINGS ///

from menus import *
from interfaces import *

#   NB FOR FUTURE PRACTICES: When reading a char from a config file, call that SPECIFIC character
#                          : location, even if the line only contains 1 character.

if linecache.getline('config.txt', 2).capitalize()[0] == "P":
    TiPl = "PLANNER"

#   /// COMPUTE CHOICES ///

if linecache.getline('config.txt', 1).capitalize()[0] == "G":
    nogui = False
    wdwProg()

while nogui == True:
    os.system(clr)
    choice = mnLaunch(TiPl)
    choice = int(choice)

#============CHOICE 1==============

    if choice == 1:
        os.system(clr)
        print("-----UNDER CONSTRUCTION, RETURNING TO MENU-----")
        time.sleep(1)

#============CHOICE 2==============    

    elif choice == 2:
        os.system(clr)
        print("ENTERING OPEN MENU...")
        time.sleep(1)
        dir = mnOpen()
        wdwProg()

#============CHOICE 3==============

    elif choice == 3:
        os.system(clr)
        print("CLEARING CONFIG FILE...\n")
        rm("config.txt")
        time.sleep(0.5)
        print("DONE!\n")
        time.sleep(1)
        print("=== EXITING ===")
        time.sleep(0.3)
        os.system(clr)
        break

#============CHOICE 4==============

    elif choice == 4:
        os.system(clr)
        yn = mnPrompt("WARNING","Are you sure you want to exit the script? [Y/N]")
        if yn in ["Y","y"]:
            os.system(clr)
            break
        else:
            os.system(clr) 
            continue

#============FALLBACK==============

    else:
        os.system(clr)
        print("! Choice invalid, please try again !")
        time.sleep(1)

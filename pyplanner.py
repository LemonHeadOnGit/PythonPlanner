#   BetterTimetable: Version 0.1.2
#   Change for your personal timetable, remove any components if necessary but do not remove Day 1.
#   Support for different configurations without modifying the code coming sometime later.
#
#   ///IMPORT MODULES

import datetime
import os
from menus import *

#   ///CREATE VARIABLES

f = os.path.isfile
rm = os.remove
fExist = True
TP = "T"
TiPl = "TIMETABLE"

#   ///WRITE TO (OR CREATE) CONFIG FILE

if f("config.txt") == True:
    open("config.txt", "r")
else:
    print("No config file detected, creating...\n\n\n")
    config = open("config.txt", "w+")
    fExist = False

#   ///PROCEED WITH PLANNER SETUP

if fExist == False:
    cfgpar = input("Would you like the Normal [N] or (INDEV) Clear [C] view?\n=====\nCHOICE: ")
    print("=====\n")
    if cfgpar not in ["N","n","C","c"]:
        print("Invalid choice, defaulting to Normal.")
        cfgpar = "N"
    config.write(cfgpar)
    # -----
    cfgpar = input("Would you like Timetable [T] or Planner [P] mode?\n=====\nCHOICE: ")
    print("=====\n")
    if cfgpar not in ["T","t","P","p"]:
        print("Invalid choice, defaulting to Planner.")
        cfgpar = "P"
    config.write(cfgpar)
    TP = cfgpar
    # -----
    config.close()

    # DO SOME THINGS

if TP in ["P","p"]:
    TiPl = "PLANNER"

choice = mnLaunch(TiPl)

#   ///COMPUTE CHOICES

choice = int(choice)

if choice == 1:
    print("-----UNDER CONSTRUCTION, EXITING-----")

elif choice == 2:
    print("ENTERING OPEN MENU...")

elif choice == 3:
    print("CLEARING CONFIG FILE...\n")
    rm("config.txt")
    print("DONE!\n")
    print("=== EXITING ===")

elif choice == 4:
    yn = mnPrompt("WARNING","Are you sure you want to exit the script? [Y/N]")
    print("EXITING...")
    
else: print("Choice invalid, exiting...")

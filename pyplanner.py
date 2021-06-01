#   BetterTimetable: Version 0.1.2
#   Change for your personal timetable, remove any components if necessary but do not remove Day 1.
#   Support for different configurations without modifying the code coming sometime later.
#
#   /// IMPORT MODULES

import os
import datetime
import time
import linecache
from menus import *
import guitest

#   /// CREATE VARIABLES NEEDED

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
    cfgpar = input("Would you like the Normal [N] or (INDEV) Clear [C] view?\n=====\nCHOICE: ")
    print("=====\n")
    if cfgpar not in ["N","n","C","c"]:
        print("Invalid choice, defaulting to Normal.")
        cfgpar = "N"
    config.writelines(cfgpar+"\n")
    
    cfgpar = input("Would you like Timetable [T] or Planner [P] mode?\n=====\nCHOICE: ")
    print("=====\n")
    if cfgpar not in ["T","t","P","p"]:
        print("Invalid choice, defaulting to Planner.")
        cfgpar = "P"
    config.writelines(cfgpar)
    TP = cfgpar
    
    config.close()

#   /// DO SOME THINGS

TP = linecache.getline('config.txt', 2)
print(TP)
time.sleep(1)
if TP in ["P","p"]:
    TiPl = "PLANNER"

#   /// COMPUTE CHOICES

while True:
    os.system(clr)
    choice = mnLaunch(TiPl)
    choice = int(choice)

    if choice == 1:
        os.system(clr)
        print("-----UNDER CONSTRUCTION, RETURNING TO MENU-----")
        time.sleep(1)
    
    elif choice == 2:
        os.system(clr)
        print("ENTERING OPEN MENU...")
        time.sleep(1)
        dir = mnOpen()
        guitest.wdwProg()

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

    elif choice == 4:
        os.system(clr)
        yn = mnPrompt("WARNING","Are you sure you want to exit the script? [Y/N]")
        if yn in ["Y","y"]:
            os.system(clr)
            break
        else:
            os.system(clr) 
            continue

    else:
        os.system(clr)
        print("! Choice invalid, please try again !")
        time.sleep(1)
        
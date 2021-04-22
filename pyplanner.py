#   BetterTimetable: Version 0.1.2
#   Change for your personal timetable, remove any components if necessary but do not remove Day 1.
#   Support for different configurations without modifying the code coming sometime later.
#
#   ///IMPORT MODULES

import datetime
import os
import menus

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
    cfgpar = input("Would you like the Normal [N] or (INDEV) Clear [C] view?\n=====\nCHOICE:")
    print("=====\n")
    if cfgpar not in ["N","n","C","c"]:
        print("Invalid choice, defaulting to Normal.")
        cfgpar = "N"
    config.write(cfgpar)
    # -----
    cfgpar = input("Would you like Timetable [T] or Planner [P] mode?\n=====\nCHOICE:")
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

print("╔═══════════════╗\n║ PYTHONPLANNER ║\n╚═══════════════╝")
config = open("config.txt", "r")
print("===== MENU =====\n\n[1] CREATE NEW", TiPl, "\n[2] OPEN", TiPl, "\n[3] EDIT CONFIG FILE\n[4] EXIT")
config.close()
choice = input("\nCHOICE: ")

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
    yn = menus.mnPrompt("WARNING","Are you sure you want to exit the script? [Y/N]")
    print("EXITING...")
else: print("Choice invalid, exiting...")

#file = int(file)
#if file == 0: 
#    day1 = "Day One: [Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
#    day2 = "Day Two: [Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
#    day3 = "Day Three: [Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
#    day4 = "Day Four: [Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
#    day5 = "Day Five: [Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
#    day6 = "Day Six: [Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"
#    day0 = "Day Zero: [Subject 1]\n[Subject 2]\n[Subject 3]\n[Subject 4]\n[Subject 5]"

#   End.
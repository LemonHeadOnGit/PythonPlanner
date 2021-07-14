#   File for the calling of text-based menus.
#   This is gonna be fun~

from termcolor import colored

def mnPrompt(title,msg):
    """A generic prompt menu"""
    print("=====",title,"=====\n")
    print(msg+"\n")
    choice = input("CHOICE: ")
    return choice

def mnLaunch(TiPl):
    """The launch menu"""
    print(colored("╔═══════════════╗","red"))
    print(colored("║ PYTHONPLANNER ║","green"))
    print(colored("╚═══════════════╝","blue"))
    config = open("config.txt", "r")
    print("===== MENU =====\n\n[1] CREATE NEW", TiPl, "\n[2] OPEN", TiPl, "\n[3] EDIT CONFIG FILE\n[4] EXIT")
    config.close()
    choice = input("\nCHOICE: ")
    return choice

def mnOpen():
    """Open a user-specified file"""
    print("===== SPECIFY THE FILENAME AND PATH TO THE PLANNER.TXT FILE =====\n")
    dir = input("DIRECTORY: ")
    return dir

print("Looks like you didn't run pyplanner.py. What're we gonna do about that now huh?")
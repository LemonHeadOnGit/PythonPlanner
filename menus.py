#   File for the calling of text-based menus.
#   This is gonna be fun~

def mnPrompt(title,msg): # This is a generic prompt menu.
    print("=====",title,"=====\n")
    print(msg+"\n")
    choice = input("CHOICE: ")
    return choice

def mnLaunch(TiPl): # This is the launch menu.
    print("╔═══════════════╗\n║ PYTHONPLANNER ║\n╚═══════════════╝")
    config = open("config.txt", "r")
    print("===== MENU =====\n\n[1] CREATE NEW", TiPl, "\n[2] OPEN", TiPl, "\n[3] EDIT CONFIG FILE\n[4] EXIT")
    config.close()
    choice = input("\nCHOICE: ")
    return choice

def mnOpen():
    print("===== SPECIFY THE FILENAME AND PATH TO THE PLANNER.TXT FILE =====\n")
    dir = input("DIRECTORY: ")
    return dir
#   File for the calling of text-based menus.
#   This is gonna be fun~

#   ///DEFINE VARIOUS TYPES OF MENUS

def mnPrompt(name,msg): # This is a generic prompt menu.
    print("=====",name,"=====\n")
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

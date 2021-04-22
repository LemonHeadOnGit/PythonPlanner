#   File for the calling of text-based menus.
#   This is gonna be fun~

#   ///DEFINE VARIOUS TYPES OF MENUS

def mnPrompt(name,msg):
    print("=====",name,"=====\n")
    print(msg+"\n")
    choice = input("CHOICE: ")
    return choice
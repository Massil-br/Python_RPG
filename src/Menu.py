import os
def clear_console():
    os.system('cls')

def press_enter():
    input("Press ENTER to continue")

def press_enter_clear():
    press_enter()
    clear_console()

def print_main_menu():
    print ("MAIN MENU : ")
    print ("Enter the number of the choice you want : ")
    print("1. Create New Game")
    print("2. Load Saved Game")
    print("3. About")
    print("4. Exit")


def print_init_menu():
    press_enter_clear()
    print("Welcome to the universe of Makatsuko, you just woke up in the middle of the forrest with only trees surrounding you.")
    press_enter_clear()
    print("You are looking arround you, to search if there is something, but you see no lights")
    press_enter_clear()
    print("Seems like you're in a deep point of the forest")
    press_enter_clear()
    print("You hear sounds arround you, but clearly not human, is there monsters in this forest?")
    press_enter_clear()
    print("You need to find something that can help you to defend yourself against monsters")
    press_enter_clear()
    print("You look at your feet, and you find a sword, was that sword here all that time? Is it your sword?")
    press_enter_clear()
    print("You are trying to remember how you got here, but you don't remember anything before you woke up in this forest")
    press_enter_clear()
    
   
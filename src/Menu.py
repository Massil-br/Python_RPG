import os
def clear_console():
    os.system('cls')

def press_enter():
    input("Press ENTER to continue...")

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
    print("You are looking arround you, to search if there is something, but you see no lights.")
    press_enter_clear()
    print("Seems like you're in a deep point of the forest.")
    press_enter_clear()
    print("You hear sounds arround you, but clearly not human, is there monsters in this forest?")
    press_enter_clear()
    print("You need to find something that can help you to defend yourself against monsters")
    press_enter_clear()
    print("You look at your feet, and you find a sword, was that sword here all that time? Is it your sword?")
    press_enter_clear()
    print("You are trying to remember how you got here, but you don't remember anything before you woke up in this forest.")
    press_enter_clear()
    
def print_choice_display():
    print("Where do you want to go?")
    print("1. Go North.")
    print("2. Go East.")
    print("3. Go South.")
    print("4. Go West.")
    print("5. Exit and save.")
    print("6. Open Inventory and Use Item or equip weapon")

def print_about_msg():
    clear_console()
    print("This game is made by MASSIL BRAIK, a RPG in console where you can move in wich direction you want.")
    press_enter_clear()
    print("The objective of the game is to kill the boss in the far South and East of the forest.")
    press_enter_clear()
    print("To make your choices and move your player, you have numbers before every choice proposed.")
    press_enter_clear()
    print("You need to write the number of the choice you want, and press ENTER.")
    press_enter_clear()
    print("The map is  10 x 10 , there are 50 monsters in the beginning and the boss.")
    press_enter_clear()
    print("The monsters will always have the same level as the player, with random stats, so they will not be too strong or too weak.")
         
         
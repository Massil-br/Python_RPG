import os
from .Entity import *
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
    
def print_choices(player: "Human"):
    choosing_action = False
    player.get_position()

    if player.pos_x == 0 and player.pos_y == 0:
        choosing_action = True
        
        while choosing_action:
            print("You see a little road in the north, and another in the East.")
            print("Where do you want to go?")
            print("1. Go NORTH")
            print("2. Go EAST")

            try:
                choice = input("Enter your choice (1 or 2): ")
                if choice == "1":
                    print("You head NORTH.")
                    player.go_north()
                    choosing_action = False  
                elif choice == "2":
                    print("You head EAST.")
                    choosing_action = False 
                    player.go_east()
                else:
                    print("\nInvalid choice. Please enter '1' or '2'.")
                    press_enter_clear()  
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                press_enter_clear()     
                
         
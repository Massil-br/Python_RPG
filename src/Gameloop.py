from .Entity import *
from enum import Enum
from .Menu import * 
class Load_or_new(Enum):
    NEW = 0
    LOAD = 1


def create_human(username) -> Human:
    player1 = Human(username,20,5)
    return player1



def create_username() -> str:
    print("Creating New Game ...")
    player = None
    username = "error"
    choosing_username = True

    while choosing_username:
        try:
            print("Please enter your username")
            username = input()
            
            if len(username) < 3:
                print("Error, your username must have at least 3 characters.")
                input("Please press Enter to try again.")
            else:
                choosing_username = False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            input("Press Enter to continue...")

        print(f"Your username is {username}")
        
    return username

    



def game_loop(player : "Human", load_or_new : "Load_or_new"):
    if load_or_new == Load_or_new.NEW:
        print_init_menu()
            
    print_choices(player)    
    
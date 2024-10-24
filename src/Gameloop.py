from .Entity import *
from enum import Enum
from .Menu import * 
class Load_or_new(Enum):
    NEW = 0
    LOAD = 1


def create_human(username) -> Human:
    player1 = Human(username,20,5)
    return player1



def create_username()-> str:
    print("Creating New Game ...")
    player = None
    choosing_username = True
    username = "error"
    while choosing_username:
        print("Please enter your username")
        username = input()
        if len(username) < 3:
            print("Error, your username must have at least 3 chars")
            input("Please press Enter to continue")
        else:
            choosing_username = False
            break
    print(f"your username is {username}")
    if username != "error":
        return username
    else: 
        print("error while sending the username")



def game_loop(player : "Human", load_or_new : "Load_or_new"):
    if load_or_new == Load_or_new.NEW:
        print_init_menu()
            
        
    
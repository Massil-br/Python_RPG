from .Entity import *
from enum import Enum
from .Menu import * 
class Load_or_new(Enum):
    NEW = 0
    LOAD = 1


def create_human(username) -> Human:
    player1 = Human(username,20,5)
    return player1

def create_classic_monster(player : "Human", name : str)-> "Monster":
    classic_monster = Monster(name, 15, 4, player.level)
    return classic_monster


def start_combat(player: "Human", monster : "Monster"):
    combat = True
    while combat :
        print("\nYou : ")
        player.present()
        print("\nEnemy : ")
        monster.present()
        print("\nWhat do you wan to do? ")
        print("1. Attack.")
        print("2. Use an Item")
        print("3. Run away.")
        choice = input("Enter your choice :")
        if choice == "1":
            player.attack(monster)
            print(f"You are attacking {monster.name}")
            
                
        elif choice == "2" :
            item_choosing = True
            while item_choosing:
                if len(player.backpack <= 0):
                    item_choosing = False
                    break
                for i , item in player.backpack:
                    print(f"{i} , {item}")
                input("choose the number of the item you want")        
        elif choice == "3":
            print("You are running away !")
            combat = False
        else:
            print("Enter a correct choice :")
            press_enter_clear()
        

        
    



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



def print_choices(player: "Human"):
    game_loop = True
    choosing_action = False
    player.get_position()
    while game_loop:
        match (player.pos_x, player.pos_y):
            case  (5, 5):
                choosing_action = True
            
                while choosing_action:
                    press_enter_clear()
                    print("You see a little road in the north, and another in the East.")
                    print("Where do you want to go?")
                    print("1. Go North")
                    print("2. Go East")
                    print("3. Exit and save")
                    choice = input("Enter your choice : ")
                    if choice == "1":
                        print("You head North.")
                        player.go_north()
                        choosing_action = False  
                    elif choice == "2":
                        print("You head East.")
                        choosing_action = False 
                        player.go_east()
                    elif choice == "3":
                        players =[player]
                        save_game(players, "mysave")
                        choosing_action = False
                        game_loop = False
                    else:
                        print("\nInvalid choice. Please enter a the number of a valid choice.")
                        press_enter_clear()    
            case (5,6):
                choosing_action = True
                while choosing_action:
                    press_enter_clear()
                    print("You see a monster in front of you, it is a wolf with two heads, you see an escape in the south, and another in the west.")
                    print("What do you want to do?")
                    print("1. Go South")
                    print("2. Go West")
                    print("3. Attack the monster")
                    print("4. Exit and save the game")
                    choice = input("Enter your choice : ")
                    if choice == "1":
                        print("You head South.")
                        player.go_south()
                        choosing_action = False
                    elif choice == "2":
                        print("You head West.")
                        player.go_west()
                        choosing_action = False
                    elif choice == "3" :
                        press_enter_clear()
                        classic_monster = create_classic_monster(player,"Double_head_wolf")
                        start_combat(player, classic_monster)
                    else:
                        print("\nInvalid choice. Please enter a the number of a valid choice.")
                        press_enter_clear() 
            case _:
                choosing_action = False
                game_loop = False 
                    
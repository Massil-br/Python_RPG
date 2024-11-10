from .Entity import *
from enum import Enum
from .Menu import *
from .Give import *
class Load_or_new(Enum):
    NEW = 0
    LOAD = 1

def game_over():
    print("You are Dead ! ")
    
def create_human(username) -> Human:
    player1 = Human(username,50,8)
    return player1

def create_classic_monster(player : "Human", name : str)-> "Monster":
    classic_monster = Monster(name, random.randint(10,30),random.randint(1,6),player.level)
    return classic_monster

def create_all_monsters(player: "Human", name: str) -> list["Monster"]:
    monsters: list["Monster"] = []
    forbidden_positions = {(5, 5), (10, 10)}  # Add any additional forbidden positions here
    used_positions = set()  # Use a set for O(1) average time complexity for lookups
    boss = Monster("Boss", 50,15,25)
    boss.pos_x = 10
    boss.pos_y = 10
    monsters.append(boss)
    for i in range(50):
        monster = create_classic_monster(player, name)
        attribute_pos = True
        while attribute_pos:
            x = random.randint(0, 20)  # Adjust the range as needed
            y = random.randint(0, 20)  # Adjust the range as needed
            position = (x, y)
            if position not in forbidden_positions and position not in used_positions:
                used_positions.add(position)  # Mark the position as used
                monster.pos_x = position[0]
                monster.pos_y = position[1] # Assign position to the monster
                attribute_pos = False  # Break the loop as position is valid
        monsters.append(monster)
    return monsters
            
def start_combat(player: "Human", monster : "Monster"):
    monster.reajust_level(player)
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
                    print("you don't have items in your backpack")
                else :
                    for i , item in player.backpack:
                        print(f"{i} , {item}")
                    input("choose the number of the item you want")        
        elif choice == "3":
            print("You are running away !")
            combat = False
            break
        else:
            print("Enter a correct choice :")
            press_enter_clear()
        print("\nYou : ")
        player.present()
        print("\nEnemy : ")
        monster.present()
        press_enter_clear()
        if not monster.is_alive:
            player.gain_xp()
            break
        monster.attack(player)
        print("\nYou : ")
        player.present()
        print("\nEnemy : ")
        monster.present()
        press_enter_clear()
        if not player.is_alive : 
            break

def create_save_name() -> str:
    save_name = ""
    choosing_save_name = True
    save_folder = 'saves'
    while choosing_save_name:
        try:
            print("Enter the name of your save :")
            save_name = input().strip()
        
            os.makedirs('saves', exist_ok=True)
            filename = os.path.join(save_folder, f"{save_name}.json")
            if len(save_name) < 3:
                print("The name of your save musst have at leat 3 characters.")
                press_enter_clear()
            elif os.path.exists(filename):
                print(f"the save name {filename} already exists, please enter another save_name")
                press_enter_clear()
            else:
                print(f"The save name of this game is {save_name}")
                choosing_save_name = False
                press_enter_clear()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            press_enter_clear()
    return save_name
            
              
def create_username() -> str:
    print("Creating New Game ...")
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
            press_enter_clear()
    print(f"Your username is {username}")
    return username

def game_loop(player: "Human", load_or_new: "Load_or_new"):
    save_name =""
    if load_or_new == Load_or_new.NEW:
        save_name = create_save_name()
        print_init_menu()
        give_start_sword(player)
        monsters = create_all_monsters(player, "monster")
    elif load_or_new == Load_or_new.LOAD:
        # List available save files in the 'saves' folder
        save_folder = 'saves'
        save_files = [f for f in os.listdir(save_folder) if f.endswith('.json')]
        
        if not save_files:
            print("No save files found.")
            return
        
        print("Available saves:")
        for i, save_file in enumerate(save_files, start=1):
            print(f"{i}. {save_file}")
        
        # Prompt the player to choose a save file
        try:
            choice = int(input("Choose a save file by entering its number: ")) - 1
            if 0 <= choice < len(save_files):
                save_name = save_files[choice].replace('.json', '')
                player, monsters = load_game(save_name)
                if player is None:
                    print("Failed to load the selected game.")
                    return
            else:
                print("Invalid choice. Starting a new game instead.")
                print_init_menu()
                monsters = create_all_monsters(player, "monster")
        except ValueError:
            print("Invalid input. Starting a new game instead.")
            monsters = create_all_monsters(player, "monster")
            username = create_username()
            if username == None or username == "error":
                return
            player : "Human" = create_human(username)
            print_init_menu()
    start_loop(player, monsters, save_name)
      
def start_loop(player: "Human", monsters: list["Monster"], save_name: str):
    game_loop = True
    while game_loop and player.is_alive:
        save_game_File(player, monsters, save_name)  
        press_enter_clear()
        for monster in monsters:
            if monster.is_alive and (player.pos_x == monster.pos_x and player.pos_y == monster.pos_y):
                start_combat(player, monster)  # Initiate combat with the matching monster
                break
        if not player.is_alive:
            game_over()  
        print_choice_display()
        choice = input("Enter your choice : ")
        if choice == "1":
            print("You head North.")
            player.go_north() 
        elif choice == "2":
            print("You head East.")
            player.go_east()
        elif choice == "3":
            print("You head South")
            player.go_south()
        elif choice == "4":
            print("You head West")
            player.go_west()
        elif choice == "5":
            save_game_File(player, monsters, save_name)   
            game_loop = False
        else:
            print("\nInvalid choice. Please enter a the number of a valid choice.")
            press_enter_clear()  

def load_game(save_name: str) -> (Human, list[Entity]):  # type: ignore
    
    filename = os.path.join('saves', f"{save_name}.json")
    
    if not os.path.exists(filename):
        print(f"Save file '{filename}' not found.")
        return None, []

    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
            if not content:  # Check if the file is empty
                print("Save file is empty.")
                return None, []
            data = json.loads(content)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None, []
    except IOError as e:
        print(f"Error reading save file: {e}")
        return None, []   
    
    player = None
    monsters = []

    if not data:  # Check if the file is empty
        print("Save file is empty or corrupted.")
        return None, []
    
    for entity_data in data:
        entity_type = entity_data.get("type", "")

        if entity_type == "Human" and player is None:
            # Initialize Human player with base attributes
            player = Human(
                entity_data.get("name"),
                entity_data.get("max_health"),
                entity_data.get("strength")
            )
            player.id = entity_data.get("id")
            player.xp = entity_data.get("xp")
            player.level = entity_data.get("level")
            player.pos_x = entity_data.get("pos_x")
            player.pos_y = entity_data.get("pos_y")
            player.health = entity_data.get("health")
            player.is_alive = entity_data.get("is_alive")
            player.defense = entity_data.get("defense")

            # Load equipped weapon if available
            if "equipped_weapon" in entity_data:
                weapon_data = entity_data["equipped_weapon"]
                player.equipped_weapon = Weapon(
                    weapon_data["name"],
                    Weapon_type[weapon_data["weapon_type"].upper()],  # Convert string to Enum
                    Rarety[weapon_data["rarety"].upper()]  # Convert string to Enum
                )
                player.equipped_weapon.id = weapon_data["id"]

            # Load backpack items
            if "backpack" in entity_data:
                player.backpack = [
                    HealthPotion(item["name"], Rarety[item["rarety"].upper()], item["id"]) if item["type"] == "HealthPotion" else
                    StrengthPotion(item["name"], Rarety[item["rarety"].upper()], item["id"]) if item["type"] == "StrengthPotion" else
                    None
                    for item in entity_data["backpack"]
                ]
                for item in entity_data["backpack"]:
                    if Item.id < item["id"]:
                        Item.id = item["id"]
            else:
                print("Warning: Backpack data missing for player.")

            # Load weapon backpack items
            if "weapon_backpack" in entity_data:
                player.weapon_backpack = [
                    Weapon(
                        weapon["name"],
                        Weapon_type[weapon["weapon_type"].upper()],  # Convert string to Enum
                        Rarety[weapon["rarety"].upper()],# Convert string to Enum
                        weapon["id"]
                    )
                    for weapon in entity_data["weapon_backpack"]  
                ]
                for weapon in entity_data["weapon_backpack"]:
                    if Item.id < weapon["id"]:
                        Item.id = weapon["id"] 
                  
                
            else:
                print("Warning: Weapon backpack data missing for player.")

        elif entity_type == "Monster":
            # Initialize each Monster and add to the monsters list
            monster = Monster(
                entity_data.get("name"),
                entity_data.get("max_health"),
                entity_data.get("strength"),
                entity_data.get("level")
            )
            monster.id = entity_data.get("id")
            monster.health = entity_data.get("health", monster.max_health)
            monster.is_alive = entity_data.get("is_alive", True)
            monster.defense = entity_data.get("defense")
            monster.pos_x = entity_data.get("pos_x")
            monster.pos_y = entity_data.get("pos_y")
            monsters.append(monster)
    print(player.name)
    print("Game loaded successfully.")
    return player, monsters

                 

def save_game_File(player:"Human", monsters: list["Monster"], save_name: str):
    save =[player]
    for monster in monsters:
        if monster.is_alive:
            save.append(monster)
    save_game(save, save_name)
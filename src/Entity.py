
import os
import json
import random
from .Item import *
from typing import TYPE_CHECKING, List
from .map import Map
if TYPE_CHECKING:
    from Item import *

def limit_map_msg():
    print("You can't go further in this direction, a magic barrier is retaining you.")

class Entity : #top Entity  mother class
    level_ratio = 1.2
    id = 0
    def __init__(self, name:str, max_health:int, strength:int):
        self.id = Entity.id
        Entity.id +=1
        self.name = name
        self.level = 1
        self.max_health = max_health
        self.health = self.max_health
        self.is_alive = True 
        self.update_health()
        self.strength = strength
        self.defense = 2
        self.pos_x = 0
        self.pos_y = 0

    def present(self):
        print(f"{self.name}  : Lvl : {self.level}")
        print(f"Health : {self.health} / {self.max_health}")
        
    def levelup(self):
        self.level += 1
        
    def update_health(self):
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
        elif self.health > self.max_health:
            self.health = self.max_health
            
    def attack(self, target:"Entity"):
        if self.is_alive and target.is_alive:
            target.health -= (self.strength - target.defense)
            target.update_health()
            round(target.health, 2)
                
    def to_dict(self):
        """Convert the entity to a dictionary."""
        return {
            "type": self.__class__.__name__,  # Include the type of entity
            "id": self.id,
            "name": self.name,
            "max_health": self.max_health,
            "strength": self.strength,
            "level": self.level,
            "health": self.health,
            "is_alive": self.is_alive,
            "defense": self.defense,
            "pos_x": self.pos_x,
            "pos_y": self.pos_y
        }

class Human(Entity):
    def __init__(self, name:str, max_health:int, strength:int):
        super().__init__(name, max_health, strength)
        self.xp = 0
        self.max_xp = 20
        self.backpack: list["Item"] = []
        self.backpack_limit = 20
        self.weapon_backpack: list["Weapon"] = []
        self.weapon_backpack_limit = 10
        self.equipped_weapon :"Weapon"  = None
        self.map = Map(10,10)
        self.pos_x = 5
        self.pos_y = 5
    
    def equip_weapon(self, weapon: "Weapon"):
        if self.equipped_weapon is not None:
            self.strength -= self.equipped_weapon.strength_bonus # Adjust strength
            self.add_to_backpack(self.equipped_weapon)
        self.equipped_weapon = weapon
        self.strength += weapon.strength_bonus
        print(f"The {weapon.type} {weapon.name} is successfully equipped.")
    
    def add_to_backpack(self, item):
        
        if isinstance(item, Weapon):  # Checks if item is specifically a Weapon
            if len(self.weapon_backpack) < self.weapon_backpack_limit:
                self.weapon_backpack.append(item)
                print(f"{item.name} added to weapon backpack.")
            else:
                print("Weapon backpack is already full.")
        elif isinstance(item, Potion):  # Checks if item is a general Item
            if len(self.backpack) < self.backpack_limit:
                self.backpack.append(item)
                print(f"{item.name} added to backpack.")
            else:
                print("Backpack is already full.")
        else:
            print("Item type not recognized.")

    

    def use_backpack_item(self, index: int):
        if 0 <= index < len(self.backpack) and self.is_alive:
            item = self.backpack[index]
            item.use(self)
            self.backpack.pop(index)
        else:
            print("Invalid index for backpack.")

    def use_weapon_backpack_item(self, index: int):
        if 0 <= index < len(self.weapon_backpack) and self.is_alive:
            weapon = self.weapon_backpack[index]
            self.equip_weapon(weapon)
            self.weapon_backpack.pop(index)  # Optionally remove the weapon from the backpack
        else:
            print("Invalid index for weapon backpack.")
    
    def choose_inventory_and_use_item(self):
        choosing_backpack = True
        choosing_item = False
        while choosing_backpack :
            choice = input("Choose inventory type (1 for backpack, 2 for weapon backpack): ")
            
            if choice == "1":
                choosing_backpack = False
                if not self.backpack:
                    print("Backpack is empty.")
                    return
                
                for i, item in enumerate(self.backpack):
                    print(f"{i}: {item.name}")
                
                choosing_item = True
                
                while choosing_item:
                    try:
                        index = int(input("Enter the index of the item to use: "))
                        if 0 <= index < len(self.backpack):
                            self.use_backpack_item(index)
                            choosing_item = False
                            
                            return  
                        else:
                            print("Index out of range. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid index number.")
            
            elif choice == "2":
                choosing_backpack = False
                if not self.weapon_backpack:
                    print("Weapon backpack is empty.")
                    return
                
                for i, weapon in enumerate(self.weapon_backpack):
                    print(f"{i}: {weapon.name}")
                choosing_item = True
                
                while choosing_item:
                    try:
                        index = int(input("Enter the index of the weapon to equip: "))
                        if 0 <= index < len(self.weapon_backpack):
                            self.use_weapon_backpack_item(index)
                            choosing_item = False
                            return  # Exit after successfully equipping a weapon
                        else:
                            print("Index out of range. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid index number.")

                
            else:
                print("Invalid choice. Please choose 1 or 2.")

    def check_level_up(self):
        if self.xp >= self.max_xp:
            self.level += 1
            self.xp -= self.max_xp
            self.max_xp = int(self.max_xp * (2**self.level-1))  
            self.increase_difficulty()

    def increase_difficulty(self):
        self.max_health = int(self.max_health * (2 ** (self.level - 1)), 0)
        self.defense *= int(1 + (Entity.level_ratio / 15))
        self.attack *= int(1 + (Entity.level_ratio / 5))
   
   
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "xp": self.xp,
            "max_xp": self.max_xp,
            "backpack": [item.to_dict() for item in self.backpack if item is not None],
            "backpack_limit": self.backpack_limit,
            "equipped_weapon": self.equipped_weapon.to_dict() if self.equipped_weapon else None,
            "weapon_backpack": [weapon.to_dict() for weapon in self.weapon_backpack if weapon is not None],
            "weapon_backpack_limit": self.weapon_backpack_limit
        })
        return data
    
    def go_north(self):
        if self.is_alive and self.pos_y < self.map.height:
            self.pos_y -= 1
        else:
            limit_map_msg()
    
    def go_south(self):
        if self.is_alive and self.pos_y > 0:
            self.pos_y += 1
        else:
            limit_map_msg()
    
    def go_east(self):
        if self.is_alive and self.pos_x < self.map.width :
            self.pos_x += 1
        else:
            limit_map_msg()
    
    def go_west(self):
        if self.is_alive and self.pos_x > 0:
            self.pos_x -= 1 
        else:
            limit_map_msg()
    
    def get_position(self):
        print(f"you are in {self.pos_x} , {self.pos_y}")  
    
    def present(self):
        super().present()
        print(f"XP : {self.xp} / {self.max_xp}")
        print(f"Attack Damage : {self.strength}")
        print(f"Defense : {self.defense}") 
    
    def gain_xp(self):
        # XP scaling with a factor that becomes smaller as the level increases
        xp_multiplier = 1 + (self.level / 10)  # Slowly decreasing multiplier to make it harder to level up
        xp_gained = random.randint(2, 10) * xp_multiplier
        self.xp += xp_gained
        
        # You can log or return the XP gained to track it
        print(f"Gained {xp_gained:.2f} XP. Current XP: {self.xp}/{self.max_xp}")
            
class Monster(Entity):
    def __init__(self, name: str, max_health: int, strength: int, level:int):
        super().__init__(name, max_health, strength)
        
    def reajust_level(self, player: "Human"):
        self.level = player.level
        self.max_health = int(self.max_health * (2 ** (self.level - 1)))
        self.health = int(self.max_health)  
        self.strength = int(self.strength * (1 + (Entity.level_ratio / 5)) ** self.level)
        self.defense = int(self.defense *(1+(Entity.level_ratio/15))**self.level)
    
def save_game(entities_list: List[Entity], save_name: str):
    os.makedirs('saves', exist_ok=True)
    filename = os.path.join('saves', f"{save_name}.json")
    with open(filename, 'w') as f:
        # Convert all entities to dictionaries and save them in a list
        json.dump([entity.to_dict() for entity in entities_list if entity is not None], f, indent=4)
    print(f"Game saved in {filename}.")

import os
import json
from .Item import Item
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
        self.level = 0
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
    
    
    def add_to_backpack(self, item: "Item"):
        if isinstance(item, Item):  # Use Item directly, not as a string
            if len(self.backpack) < self.backpack_limit:
                self.backpack.append(item)
                print(f"{item.name} added to backpack.")
            else:
                print("Backpack is already full.")
        elif isinstance(item, Weapon):  # If it's a weapon
            if len(self.weapon_backpack) < self.weapon_backpack_limit:
                self.weapon_backpack.append(item)
                print(f"{item.name} added to weapon backpack.")
            else:
                print("Weapon backpack is already full.")
        else:
            print("Item type not recognized.")
        if self.equipped_weapon is None and isinstance(item, Weapon):
            self.equip_weapon(item)

    def equip_weapon(self, weapon: "Weapon"):
        if self.equipped_weapon is not None:
            self.strength -= self.equipped_weapon.strength_bonus
        self.equipped_weapon = weapon
        self.strength += weapon.strength_bonus
        print(f"The {weapon.type} {weapon.name} is successfully equipped.")

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

    def check_level_up(self):
        if self.xp >= self.max_xp:
            self.level +=1
            self.xp -= self.max_xp
            self.max_xp * Entity.level_ratio
            self.defense * Entity.level_ratio
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "xp": self.xp,
            "backpack": [item.to_dict() for item in self.backpack],
            "backpack_limit": self.backpack_limit,
            "equipped_weapon": self.equipped_weapon.to_dict() if self.equipped_weapon else None,
            "weapon_backpack":[weapon.todict() for weapon in self.weapon_backpack],
            "weapon_backpack_limit": self.weapon_backpack_limit
        })
        return data
    
    def go_north(self):
        if self.is_alive and self.pos_y < self.map.height:
            self.pos_y += 1
        else:
            limit_map_msg()
    
    def go_south(self):
        if self.is_alive and self.pos_y > 0:
            self.pos_y -= 1
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
            
class Monster(Entity):
    def __init__(self, name: str, max_health: int, strength: int, level:int):
        super().__init__(name, max_health, strength)
        self.level = level
        self.max_health +=((max_health * Entity.level_ratio)*self.level)
        self.health = self.max_health
        self.strength +=((self.strength * Entity.level_ratio)*self.level)
        self.defense += ((self.strength * Entity.level_ratio)*self.level)    
    
    
def save_game(entities_list: List[Entity], save_name: str):
    os.makedirs('saves', exist_ok=True)
    filename = os.path.join('saves', f"{save_name}.json")

    with open(filename, 'w') as f:
        # Convert all entities to dictionaries and save them in a list
        json.dump([entity.to_dict() for entity in entities_list if entity is not None], f, indent=4)

    print(f"Game saved in {filename}.")
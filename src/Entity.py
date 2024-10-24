
import os
import json
from .Item import Item
from typing import TYPE_CHECKING, List
from .map import Map


if TYPE_CHECKING:
    from Item import *




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
        print(f"ID : {self.id}")
        print(f"hello my name is {self.name}")
        print(f"i am level {self.level}")
        print(f"i have {self.strength} of strength")
        print(f"Health : {self.health}")
    
    def levelup(self):
        self.level += 1
    
    def update_health(self):
        if self.health < 0:
            self.health = 0
            self.is_alive = False
        elif self.health > self.max_health:
            self.health = self.max_health
    def attack(self, target:"Entity"):
        if self.is_alive:
            target.health -= (self.strength - target.defense)
            target.update_health()
            
    def to_dict(self):
        """Convert the entity to a dictionary."""
        return {
            "type": self.__class__.__name__,  # Include the type of entity
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
        self.backpack: List["Item"] = []
        self.backpack_limit = 20
        self.equipped_weapon :"Weapon"  = None
        self.map = Map(10,10)
        self.pox_x = 5
        self.pos_y = 5
    
    
    def add_to_backpack(self, item: "Item"):
        if isinstance(item, "Item"):
            if len(self.backpack) < self.backpack_limit:
                self.backpack.append(item)
            else:
                print("backpack allready full")
            if self.equipped_weapon == None and isinstance(item, "Weapon"):
                self.equip_weapon(item)
                
    def equip_weapon(self, weapon:"Weapon"):
        if self.equipped_weapon is not None:
            self.strength -= self.equipped_weapon.strength_bonus  
        self.equipped_weapon = weapon
        self.strength += weapon.strength_bonus       
        print(f"the {weapon.type} {weapon.name} is successfully equipped")    
                
    def use_backpack_item(self, index:int):
        if 0 <= index < len(self.backpack) and self.is_alive:
            item = self.backpack[index]
            item.use(self)
            self.backpack.pop(index)
            
        else:
            print("Index invalide pour le sac à dos")

   
    def check_level_up(self):
        if self.xp >= self.max_xp:
            self.level +=1
            self.xp = (self.xp-self.max_xp)
            self.max_xp * Entity.level_ratio
            self.defense * Entity.level_ratio
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "xp": self.xp,
            "backpack": [item.to_dict() for item in self.backpack],
            "equipped_weapon": self.equipped_weapon.to_dict() if self.equipped_weapon else None
        })
        return data
    
    
    def go_north(self):
        if self.is_alive and self.pos_y < self.map.height:
            self.pos_y += 1
    
    def go_south(self):
        if self.is_alive and self.pos_y > 0:
            self.pos_y -= 1
    
    def go_east(self):
        if self.is_alive and self.pos_x < self.map.width :
            self.pos_x += 1
    
    def go_west(self):
        if self.is_alive and self.pos_x > 0:
            self.pos_x -= 1 
    
    
    def get_position(self):
        print(f"you are in {self.pos_x} , {self.pos_y}")     
            
    
class Monster(Entity):
    def __init__(self, name: str, max_health: int, strength: int, level:int):
        super().__init__(name, max_health, strength)
        self.level = level
        self.max_health +=((max_health * Entity.level_ratio)*self.level)
        self.strength +=((self.strength * Entity.level_ratio)*self.level)
        self.defense += ((self.strength * Entity.level_ratio)*self.level)    
    
    def to_dict(self):
        return super().to_dict()
    
    
    



def save_game(entities_list: List[Entity], save_name: str):
    os.makedirs('saves', exist_ok=True)
    filename = os.path.join('saves', f"{save_name}.json")

    with open(filename, 'w') as f:
        # Convert all entities to dictionaries and save them in a list
        json.dump([entity.to_dict() for entity in entities_list if entity is not None], f, indent=4)

    print(f"Game saved in {filename}.")
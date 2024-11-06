from typing import TYPE_CHECKING
from enum import Enum
if TYPE_CHECKING:
    from .Entity import Entity
      
class Rarety(Enum):
    IRON = "iron"
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"
    DIAMOND = "diamond"

class Weapon_type(Enum):
    DAGGER = "dagger"
    SWORD = "sword"
    BOW = "bow"

class Item: #top item  mother class
    id = 0
    def __init__(self, name: str):
        self.id = Item.id
        Item.id += 1
        self.name = name
        
    def use(self, entity: "Entity"):
        pass

class Potion(Item):
    rarety_power_map = {
        Rarety.IRON: 5,
        Rarety.BRONZE: 10,
        Rarety.SILVER: 20,
        Rarety.GOLD: 30,
        Rarety.DIAMOND: 50
    }
    
    def __init__(self, name: str, rarety: Rarety):
        super().__init__(name)
        self.power = Potion.rarety_power_map.get(rarety, 0)
    
    def use(self, entity: "Entity"):
        pass

class HealthPotion(Potion):   
    def use(self, entity: "Entity"):
        entity.health = min(entity.health + self.power, entity.max_health)

class StrengthPotion(Potion):
    def use(self, entity:"Entity"):
        entity.strength += self.power
        
class Weapon(Item):
    rarety_power_map = {
        Rarety.IRON: 2,
        Rarety.BRONZE: 5,
        Rarety.SILVER: 10,
        Rarety.GOLD: 25,
        Rarety.DIAMOND: 40
    }
    
    def __init__(self, name: str , type : Weapon_type  , rarety : Rarety ):
        super().__init__(name)
        self.type = type
        self.rarety = rarety
        self.strength_bonus = Weapon.rarety_power_map.get(self.rarety , 0)

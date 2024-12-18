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

class Item:
    id = 0
    def __init__(self, name: str, id = None ):
        if id is not None:
            self.id = id
        else:
            self.id = Item.id
            Item.id += 1
        self.name = name
        
    def use(self, entity: "Entity"):
        pass
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Potion(Item):
    rarety_power_map = {
        Rarety.IRON: 5,
        Rarety.BRONZE: 10,
        Rarety.SILVER: 20,
        Rarety.GOLD: 30,
        Rarety.DIAMOND: 50
    }
    
    def __init__(self, name: str, rarety: Rarety,id=None):
        if id == None:
            super().__init__(name)
        else:
            super().__init__(name, id)
        self.power = Potion.rarety_power_map.get(rarety, 0)
    
    def use(self, entity: "Entity"):
        pass

class HealthPotion(Potion):   
    def use(self, entity: "Entity"):
        entity.health = min(entity.health + self.power, entity.max_health)
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "HealthPotion",
            "power": self.power
        })
        return data

class StrengthPotion(Potion):
    def use(self, entity: "Entity"):
        entity.strength += self.power
        entity.buff += self.power
        entity.buff_time += 3
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "StrengthPotion",
            "power": self.power
        })
        return data

class Weapon(Item):
    rarety_power_map = {
        Rarety.IRON: 2,
        Rarety.BRONZE: 5,
        Rarety.SILVER: 10,
        Rarety.GOLD: 25,
        Rarety.DIAMOND: 40
    }
    
    def __init__(self, name: str, type: Weapon_type, rarety: Rarety, id=None ):
        if id == None:
            super().__init__(name)
        else:
            super().__init__(name, id)
        self.type = type
        self.rarety = rarety
        self.strength_bonus = Weapon.rarety_power_map.get(self.rarety, 0)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "type": "Weapon",
            "weapon_type": self.type.name,
            "rarety": self.rarety.name,
            "strength_bonus": self.strength_bonus
        })
        return data

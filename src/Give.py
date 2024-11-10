from .Item import *
from .Entity import Human

def give_start_sword(player: "Human"):
    start_sword = Weapon("Starter Sword", Weapon_type.SWORD, Rarety.BRONZE )
    player.add_to_backpack(start_sword)
    player.equip_weapon(start_sword)
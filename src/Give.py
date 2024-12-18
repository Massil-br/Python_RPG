from .Item import *
from .Entity import Human
import random
from .Menu import press_enter_clear

def give_start_sword(player: "Human"):
    start_sword = Weapon("Starter Sword", Weapon_type.SWORD, Rarety.BRONZE )
    player.add_to_backpack(start_sword)
    player.use_weapon_backpack_item(0)
    
def give_drop(player:"Human"):
    potion : "Potion" = drop_potion()
    weapon : "Weapon" = drop_weapon()
    if not potion == None :
        player.add_to_backpack(potion)
        print(f"you dropped a {potion.power} power {potion.name}")
        press_enter_clear()
    
    if not weapon == None :
        player.add_to_backpack(weapon)
        print(f"you dropped a {weapon.strength_bonus} power {weapon.name}")
        press_enter_clear()
        
def drop_potion()-> Potion: 
    potion :Potion
    rarety : Rarety
    drop_potion = random.randint(0,100)
    rarety_rand = random.randint(0,100)
    if rarety_rand >80 :
        rarety = Rarety.DIAMOND
    elif rarety_rand >60 :
        rarety = Rarety.GOLD
    elif rarety_rand > 40 :
        rarety = Rarety.SILVER
    elif rarety_rand > 20 :
        rarety = Rarety.BRONZE
    else:
        rarety = Rarety.IRON
        
        
    if drop_potion >75:
        potion = StrengthPotion("StrengthPotion", rarety)
    elif drop_potion > 50:
        potion = HealthPotion("HealthPotion", rarety)
    else:
        potion = None  
        
    return potion   

def drop_weapon() -> Weapon:
    drop_weapon_int = random.randint(0,100)
    weapon_type_int = random.randint(0,100)
    rarety_rand = random.randint(0,100)
    rarety :Rarety
    weapon_type: Weapon_type
    weapon :Weapon
    weapon_name =""
    if weapon_type_int > 67:
        weapon_type = Weapon_type.BOW
        weapon_name = "BOW"
    elif weapon_type_int > 33 :
        weapon_type = Weapon_type.DAGGER
        weapon_name = "DAGGER"
    else:
        weapon_type = Weapon_type.SWORD
        weapon_name = "SWORD"
    
    if rarety_rand >95 :
        rarety = Rarety.DIAMOND
    elif rarety_rand >80 :
        rarety = Rarety.GOLD
    elif rarety_rand > 50 :
        rarety = Rarety.SILVER
    elif rarety_rand > 30 :
        rarety = Rarety.BRONZE
    else:
        rarety = Rarety.IRON
        
    if drop_weapon_int > 75 :
        weapon = Weapon(weapon_name, weapon_type, rarety)
    else :
        weapon = None
    
    return weapon
                   
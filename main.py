#This is for testing my python skills
#will attempt to make a short game where you defeat a monster after equipping a weapon of your choosing

#Making the Monster class
class Monster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        
monster1 = Monster("Monster 1", 100, 10)


#Making the Player class
class Player:
    def __init__(self, name, health, base_damage, exp, current_level):
        self.name = name
        self.health = health
        self.base_damage = base_damage
        self.exp = exp
        self.current_level = current_level
    #Creating the Weapon class for the player to equip
    class Weapons:
        def __init__(self, name, damage):
            self.name = name
            self.damage = damage
    sword = Weapons("sword", 10)
    axe = Weapons("Axe", 30)
    
    
player = Player("Name Here", 100, 5, 0, 1)

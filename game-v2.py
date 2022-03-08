#This is for testing my python skills
#will attempt to make a short game where you defeat a monster after equipping a weapon of your choosing

#Making the Weapons class
class Weapons:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
sword = Weapons("sword", 10)
axe = Weapons("Axe", 30)
    

#Making the Monster class
class Monster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        
monster = Monster("Monster 1", 100, 10)


#Making the Player class
class Player:
    def __init__(self, name, health, base_damage, exp, current_level):
        self.name = name
        self.health = health
        self.base_damage = base_damage
        self.exp = exp
        self.current_level = current_level
    #This is where the player equips the weapong of his choosing
    def Weapon_Equip(self):
        equip = input("Would you like to equip a weapon?: ")
        if equip.lower() == "yes":
            equip = input("Which weapon? Sword or Axe?: ")
            if equip.lower() == "sword":
                self.base_damage = self.base_damage + sword.damage
                print("Post Weapon Equip Damage: " + str(self.base_damage))
            if equip.lower() == "axe":
                self.base_damage = self.base_damage + axe.damage
                print("Post Weapon Equip Damage: " + str(self.base_damage))
        if equip.lower() == "no":
            print("You've chosen to not equip a weapon")
            print("Regular Base Damage: " + str(self.base_damage))
    #This is where the player attacks the Monster
    def Attack(self):
        attack = input("Would you like to attack the monster?: ")
        if attack.lower() == "yes":
            if monster.health > 0:
                monster.health = monster.health - self.base_damage
                print("Monster Health: " + str(monster.health))
            elif monster.health == 0:
                print("You have defeated the monster!")
            else:
                print("You have defeated the monster!")
        if attack.lower() == "no":
            print("You've decided to not attack the monster")
        
    

player = Player("Name Here", 100, 5, 0, 1)
def Game():
    player.Weapon_Equip()
    if monster.health > 0:
        player.Attack()
    if monster.health > 0:
        player.Attack()
    if monster.health > 0:
        player.Attack()
    if monster.health > 0:
        player.Attack()
    if monster.health > 0:
        player.Attack()
Game()

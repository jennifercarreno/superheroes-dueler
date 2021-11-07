import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):

        if len(self.abilities) == 0 or len(opponent.abilities) == 0:
            print(f"draw")
        else: 
            while self.current_health > 0 or opponent.current_health > 0:
                total_damage = self.attack()
                opponent.take_damage(total_damage)

                if opponent.is_alive() == True:
                    total_damage = opponent.attack()
                    self.take_damage(total_damage)

                    if self.is_alive == True:
                        total_damage = total_damage = self.attack()
                        opponent.take_damage(total_damage)
                    else:
                        # print(self.current_health)
                        return print(f"{opponent.name} Won!")
                elif opponent.is_alive() == False: 
                    # print(opponent.current_health)
                    return print(f"{self.name} Won!")

    
    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)
    
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        total_block = 0
        if self.current_health == 0:
            total_block = 0 
        else: 
            for armor in self.armors:
                total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        defence = self.defend()
        new_damage = damage - defence
        # print(self.current_health)
        # print(f"this is new damage: {new_damage}")
        if new_damage > 0: 
            self.current_health -= new_damage
            return self.current_health
        else:
            return "no damage taken"
    
    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True




if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)

import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

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
                        opponent.kills+=1
                        self.deaths+=1
                        return print(f"{opponent.name} Won!")
                elif opponent.is_alive() == False: 
                    # print(opponent.current_health)
                    self.kills +=1
                    opponent.deaths+=1
                    return print(f"{self.name} Won!")

    
    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        self.kills += num_kills
    
    def add_death(self, num_deaths):
        self.deaths += num_deaths
    
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
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())

import random
class character:
    def __init__(self, name, st, tou, luc, dex):
        self.name = name
        self.strength = st  # out of 5
        self.toughness = tou  # out of 5
        self.luck = luc  # out of 3
        self.dexterity = dex  # out of 5
        self.health = 20

    def get_name(self):
        return self.name

    def set_name(self, n):
        self.name = n

    def attack(self, opponent):

        attribute = random.randint(0,0) #0 = strength, 1 = toughness, 2= dexterity
        if attribute == 0:
            #strength
            if self.strength+(1*self.luck) > opponent.strength+(1*opponent.luck):
                print( f"{self.get_name()} wins in a battle of strength!")
                damage = random.randint(1,self.luck)
                print(f"{self.get_name()} deals {damage} points of damage to {opponent.get_name()}!")
                opponent.health = opponent.health - damage
            else:
                print(f"{opponent.get_name()} wins in a battle of strength!")
                damage = random.randint(1, opponent.luck)
                print(f"{opponent.get_name()} deals {damage} points of damage to {self.get_name()}!")
                self.health = self.health - damage
        elif attribute == 1:
            #toughness
            pass
        else:
            #dexterity
            pass
    def enter(self):
        output = random.choice([f"I'm {self.get_name()}. It's time to kick ass and chew bubble gum, and I'm all out of gum...",f"I'm {self.name}, and I have come to chop you into tiny little bits!"])
        return output

    def exit(self):
        return "Let's do it again. BRING IT ON!"
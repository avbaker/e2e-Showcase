class character():
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

    def attack(self, opponent, ):

    def enter(self):
        return f"I'm {self.get_name()}. It's time to kick ass and chew bubble gum, and I'm all out of gum..."

    def exit(self):
        return "Let's do it again. BRING IT ON!!!!1"
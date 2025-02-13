import random
from chara import *

Steve = character("Steve",3,2,2,3)
Caroline = character("Caroline",3,2,2,3)

print(Steve.enter())
print(Caroline.enter())
while Steve.health > 0 and Caroline.health >0:
    Steve.attack(Caroline)
    Caroline.attack(Steve)
    print(f"steve = {Steve.health}hp\nCaroline = {Caroline.health}hp\n\n\nPress enter to continue.")
    input()


print(Steve.exit())
# exo 1.2
# Alice et Bob veulent jouer aux dés.
# Alice parie qu'elle va faire au moins 4. Bob parie qu'il va faire 3 au plus.
# Qui gagne ? Alice ou Bob ?
# Rédigez le code qui indique le nom du gagnant.

import random

dice = random.randint(1, 6)

# réponse 1.2

print(dice)
if dice >= 4 : 
    print(f'félicitation Alice, tu as gagné')
elif dice <= 3 : 
    print(f'félicitation Bob, tu as gagné')
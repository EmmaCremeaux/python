# exo 1.3
# Alice et Bob jouent à pierre papier ciseaux.
# - 1 équivaut à pierre
# - 2 équivaut à papier
# - 3 équivaut à ciseaux
# Rédigez le code qui indique qui gagne.

import random

alice = random.randint(1, 3)
bob = random.randint(1, 3)
print(alice, bob)

# réponse 1.3
print(f'alice a tiré {alice}')
print(f'bob a tiré {bob}')
if (alice == 1 and bob == 3) or (alice == 3 and bob == 2) or (alice == 2 and bob == 1) :
    print('Alice gagne')
elif (bob == 1 and alice == 3) or (bob == 3 and alice == 2) or (bob == 2 and alice == 1) : 
    print('bob gagne')
else :
    print('egalité')

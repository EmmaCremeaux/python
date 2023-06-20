# exo 7.3
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est égal à 1

import random

# réponse 7.3
for dice in range(1, 101):
    r = random.randint(1, 10)
    print(r)
    if r == 1 : 
        print(f'r est egal à {r}')


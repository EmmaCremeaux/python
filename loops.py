import random
# while : c'est comme un "if" mais qui est répété

while False : 
    print("ce message ne s'affiche pas")
                                                # ctrl + c pour stopper la boucle infini
# while True : 
#     # permet de reprendre au debut de la boucle suivante
#     continue  
#     print("ce message est affiché en boucle")
#     # arrête la boucle
#     break
            

# premier tirage
dice = random.randint(1, 6)

while dice != 6 :
    print(f"je n'ai pas tirer un 6, mais un {dice}")
    print("je recommence un nouveau tirage")
    dice = random.randint(1, 6)

print(f"j'ai tirer un {dice}")

# recréation de la boucle for classique avec une boucle while
i = 0
while i < 10 : 
    print(f"{i = }")
    i += 1

# boucle for classique en python
for i in range(0, 10): # 0 est inclus et 10 est exclus
    print(f'{i = }')

# boucle a rebours
for i in range(10, 0, -1):
                      # le dernier -1 est une décrémentation
    print(f'{i = }')


# boucle for each
users = ['foo', 'bar', 'baz']

for user in users:
    print(user)


# enumerate permet de récupérer l'index de chaque éléments
# quelque soit le nom des variables, l'index est toujours dans la 1ere et la valeur dans la 2eme
for i, user in enumerate(users):
    print(f"{i = }, {user = }")


# boucle for
for i in range(0, len(users)):
    user = users[i]
    print(f"{i = }, {user = }")


# accumulateur 
accumulateur = 0
for i in range(1, 11) : 
    accumulateur += i
    print(f'{i = }')
    print(f'{accumulateur = }')
    print('')


# utiliser la valeur précédente dans une boucle 
numbers = [123, 42, 1000, 3.14]

    # au 1er tour il n'y a pas de valeur précédente
previous = None

for number in numbers : 
    # on affiche la valeur du tour actuelle
    print(number)
    # on affiche la valeur du tour précédent
    print(previous)

    # préparation du tour suivant
    # on sauvegarde la valeur du tour actuel pour le tour suivant
    # cette valeur deviendra la valeur du tour précédent
    previous = number
    

    
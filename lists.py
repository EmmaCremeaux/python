import random

users = ['foo', 'bar', 'baz']
mix = [True, 3.14, 'lorem ipsum', None, [123, 42]]
# equivaut a cette ecriture : 
# mix = [
#     True, 
#     3.14, 
#     'lorem ipsum', 
#     None, 
#     [123, 42]
# ]



# Accés en lecture
    # 0 est l'index du 1er élément
print(users[0])

    # len - 1 est l'index du dernier élément
i = len(users) - 1
print(users[i])

    # quand l'index depasse la taille de la liste il y a une erreur
# print(users[100 + 42]) => ERREUR


# Accés en écriture
    # remplacer un élémént existant
users[0] = "lorem"  # variable scalaire
print(users)

    # ajouter un nouvel élément (a la fin)
users.append('ipsum')
print(users)

    # ajouter un nouvel élément (a une place precise)
users.insert(0, 'sit')
users.insert(2, 'dolores')
print(users)

    # supprimer le dernier élément de la liste
last_user = users.pop()
print(last_user)
print(users)

    # supprimer un élément (par l'index)
first_user = users.pop(0)
print(first_user)
print(users)

    # supprimer un élément (par la valeur)
users.remove('bar')
print(users)



fruits = ['ananas', 'banane', 'cerise']
legumes = ['artichaud', 'brocoli', 'carotte']
ingredients = fruits + legumes
print(ingredients)

fruits += legumes
print(fruits)


# tri par ordre alphabetique ou croissant :
letters = ['g', 'd', 'a', 'c', 'b', 'Z']     # les majuscules sont toujours avant les minuscules
letters = sorted(letters)                    # CF tableau ascii (IMPORTANT)
print(letters)

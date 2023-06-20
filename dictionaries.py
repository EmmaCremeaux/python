fruits = {
    'a': 'ananas',
    'b': 'banane',
    'c': 'cerise',
}
print(fruits)


# accés en lecture
print(fruits['a'])

# accés en ecriture
fruits['a'] = 'abricot'
print(fruits)

# boucle foreach :
        # pour obtenir les clés :
for key in fruits:
    print(f'{key = }')
    # fruits[key] contient la valeur associée à la clé
    print(f'fruit = {fruits[key]}')

        # pour obtenir les clés et les valeurs en même temps :
for key, value in fruits.items():
    print(f'{key = }')
    print(f'{value = }')

        # pour obtenir que les valeurs : 
for value in fruits.values():
    print(f'{value = }')

# dictionnaire avec clés de tout type : 
my_dict = {
    100: 'foo',
    # si une même clé réapparait elle écrase la 1ere : 
    100: 'bar',
    3.14: True,
    True: 'abc',
    None: 123,
}

print(my_dict)

# ajouter une nouvelle entrée : 
my_dict['baz'] = 1
print(my_dict)

#supprimer une entrée existante sans garder de copie: 
del my_dict['baz']
print(my_dict)

#supprimer une entrée existante en gardant une copie dans une variable: 
a = my_dict.pop(3.14)
print(my_dict)

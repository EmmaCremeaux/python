import library

# définition : 
def hello():
    print('hello python!')

# appel ou exécution : 
hello()

def hello2(name):
    print(f'hello {name} !')

hello2('Foo')

def addition(a, b):
    return a + b

resultat = addition(42, 123)
print(resultat)

# appel d'une fonction stocké dans un autre module/fichier
resultat = library.oui_non(False)
print(resultat)


# reverse lookup : 
my_list = [42, 123, 3.14]

def reverse_lookup(my_list, value):
    """
    Cette fonction prend en paramètre une liste et une valeur à rechercher. 
    Elle renvoie l'index de la valeur si elle est trouvée, 
    ou None si la valeur n'est pas trouvée.

    my_list list la liste dans laquelle il faut chercher.
    value any la valeur à rechercher.
    return int ou None l'index de la valeur recherché.
    """
    for i in range(len(my_list)) : 
        if my_list[i] == value:
            return i
        
    return None

resultat = reverse_lookup(my_list, 3.14) 
print(resultat)
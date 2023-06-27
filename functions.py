import library # import d'un fichier qu'on a créer et qui contient une fonction qu'on veux réutilisé ici.

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


# type hinting : ne sert qu'a indiquer le type souhaité
# le nom de la fonction + ses paramètres + son type de retour = signature de la fonction
def mult(a: int, b: int) -> int:
    return a * b

result = mult(2, 5)
print(result)

# mais les autres type de donnée passent quand même : 
# result = mult('abc', 5)

# Copie d'une fonction comme si c'etait une fonction
mult_copy = mult
mult_copy(2, 5)


# Stockage de fonction dans une liste : 
operations = []
operations.append(addition)
operations.append(mult)

a = 2
b = 5
result = None

for operation in operations : 
    result = operation(a, b)
    print(result)


# fonction d'ordre supérieur :
# fonction qui accepte une autre fonction en paramètre 
# ou qui renvoie une fonction.
def operateur_binaire(a, b, fonction):
    return fonction(a, b)

# Appel de la fonction d'ordre superieur
resultat = operateur_binaire(2, 5, mult)
print(resultat)


my_list = ['foo', 'ispum']
text = 'toto'

print(len(my_list))
print(len(text))

def my_len(value):
    return 42

# Sauvegarde de la fonction len() originale
len_copy = len

# Surcharge de la fonction len() originale 
# = remplacement par une autre fonction 
len = my_len

print(len(my_list))
print(len(text))

# Restauration de la fonction len() originale
len = len_copy


# pass permet d'ecrire du code python syntaxiquement valide
# même quand on a pas encore le corp du if ou d'une boucle
if True : 
    pass


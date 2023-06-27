# scope = portée des variables

my_var1 = 123

def my_func1():
    print(my_var1)
    print(my_var2)

my_var2 = 42

# La fonction voit les variables définies à l'exterieur
# au préalable ou à posteriori
my_func1()


def my_func2():
    my_var3 = 3.14

my_func2()

# Il n'est pas possible d'accéder a une variable définie
# à l'intérieur d'une fonction, que celle ci est etait executé ou non.
# principe du verre teinté (comme avec une limousine)
# NameError: name 'my_var3' is not defined.
# print(my_var3)

my_var4 = 'foo'

def my_func3(my_var4):
    # le paramètre my_var4 masque la variable définie à l'exterieur de la fonction
    print(my_var4)

# Cet appel affiche 'bar'
my_func3('bar')


def my_func4():
    # la variable my_var4 fait de l'ombre (shadowing) la variable définie à l'exterieur de la fonction
    my_var4 = 'baz'
    print(my_var4)

my_func4()
# La variable my_var4 définie a l'extérieur de la fonction
# reste inchangée
print(my_var4)


def my_func5(my_var5):
    my_var5 = 'fooz'
    print(my_var5)

my_var6 = 13

# les variables de type int, float, bool ou str sont passé par valeur.
# c-à-d que la fonction ne pourra accéder qu'à une copie de la variable original définie à l'exterieur
my_func5(my_var6)
print(my_var6)

def my_func6(my_var7: list):
    my_var7.append('foo')

my_var8 = [123, 42, 3.14]
# les variables de type liste, tuple, dictionnaire ou objet sont passé par référence
# c-à-d que la fonction pourra accéder à la variable original définie à l'exterieur
my_func6(my_var8)
print(my_var8)


# exo 10.5
# Créer une fonction nommée `compare()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoie une valeur de type `int`
# - renvoie 1 si `a` est plus grand que `b`
# - renvoie -1 si `a` est plus petit que `b`
# - renvoie 0 si `a` et `b` sont égaux
# Appelez la fonction et affichez le résultat

# réponse 10.5
def compare(a: float, b: float) -> int:
    if a > b:
        return 1
    elif a < b:
        return -1
    else : 
        return 0 

verif1 = compare(9.15, 2.7)
verif2 = compare(6.7, 8.6)
verif3 = compare(5.2, 5.2)

print(verif1)
print(verif2)
print(verif3)

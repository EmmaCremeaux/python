# exo 10.4
# Créer une fonction nommée `is_greater()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoie une valeur booléenne
# - renvoie True si `a` est plus grand que `b`
# - renvoie False dans les autres cas
# Appelez la fonction et affichez le résultat

# réponse 10.4
def is_greater(a: float, b: float) -> bool:
    if a > b :
        return True
    else: 
        return False
verif1 = is_greater(2.15, 6.17)
verif2 = is_greater(5.2, 1.9)

print(verif1)
print(verif2)
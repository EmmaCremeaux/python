# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.
#
# ATTENTION : ne pas utiliser la fonction list.index()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15
longueur = 0
valeur = ''
index = None

for number in range(len(my_list)) :
    if (len(my_list[number]) > longueur): 
        longueur = len(my_list[number])
        valeur = my_list[number]
        index = number
print (f'le mot le plus long est "{valeur}" est à l\'index {index} et a une longueur de {longueur}.')

    
    
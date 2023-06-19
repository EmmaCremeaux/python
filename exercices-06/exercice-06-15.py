# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.
#
# ATTENTION : ne pas utiliser la fonction list.index()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15
print(my_list)
new_list = []
for text in range(len(my_list)) :
    new_list = new_list + [len(my_list[text])]
print(new_list)

max_value = None
for number in range(len(new_list)) :
    if (max_value is None or number >= max_value):
        max_value = new_list[number]
        index = number
my_list = my_list[index]
        
print('longueur la plus grande :', max_value)
print('index :', index)
print('valeur :', my_list)


    

  
        

    
    
    
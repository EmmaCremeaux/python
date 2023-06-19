# exo 6.16
# Ici le but est d'intervertir les éléments de la liste deux à deux
# Liste initiale :
#
#   my_list = [2.71, 42, 123, 2, 3.14, 1.61]
#
# Résultat attendu :
#
#   my_list = [42, 2.71, 2, 123, 1.61, 3.14]
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.16
new_list1 = []
new_list2 = []
for number in range(len(my_list)) :
    if number%2 == 1:
        new_list1 = new_list1 + [my_list[number]]
    else :
        new_list2 = new_list2 + [my_list[number]]
my_list = ([new_list1[0]] + [new_list2[0]] + [new_list1[1]] + [new_list2[1]] + [new_list1[2]] + [new_list2[2]])
    
    
print(f'new list 1 = {new_list1}')
print(f'new list 2 = {new_list2}')
print(f'my list = {my_list}')



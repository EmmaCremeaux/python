# exo 6.14
# Créez une deuxième liste nommée `new_list` ne contenant que les nombres entiers de la liste
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.14
new_list = []
for number in range(len(my_list)) :
    if my_list[number] == int(my_list[number]) :
        new_list = new_list + [my_list[number]]
print(new_list)

   
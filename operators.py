import random 

# Arithmétique :
a = 123 + 42
b = 123 - 42
c = 123 * 42
d = 123 / 42

print(a)
print(b)
print(c)
print(d)

# Division entière : 
e = 123 // 42
print(e)

#modulo ou reste de la divisio, (euclidienne)
# 123 = 42 * 2 + 39    # Ecriture mathématique => Le modulo c'est le reste, ici le 39.
# a = 123 % 42         # Ecriture informatique => '%' permet de demander le modulo de la division.


# vérification des nombres pair et impair
a = 53
# S'il y a un reste, le nombre n'est pas divisible par 2, donc il est impair:
print(a % 2)

a = 74
# Si il n'y a pas de reste, le nombre est divisible par 2, donc il est pair:
print(a % 2)

# Puissance : 
# 2 puissance 3 
f = 2 ** 3
print(f)

# Opérateur de comparaison : 

    # égalité : 
result1 = 123 == 123
print(result1)

password = "abc"
user_input = "def"
print(password == user_input)

    # (strictement) plus grand que : 
result2 = 123 > 42
print(result2)

    # plus grand ou égale que :
result3 = 123 >= 123
print(result3)

    # Plus petit (ou egale <=):
result4 = 42 < 123
print(result4)

    # Différent de : 
result5 = 123 != 123
print(result5)

    # opérateurs composés
b = 0

    # opérateur d'incrémentation
    # b = b + 1
b += 1
print(b)

    # b = b - 1
b -= 1
print(b)

    # Multiplication 
c = 3
    # c = c * 2
c *= 2
print(c)

    # Division
d = 10
    # d = d / 3
d /= 3 
print(d)
    
    # Division entiere 
d = 10
    # d = d // 3
d //= 3 
print(d)

    # Opérateur d'inclusion
text1 = "Lorem ipsum"

result = "e" in text1 # prend en compte les majuscules
print(result)

list1 = ['Lorem', 'ipsum']
print("e" in list1) # ici c'est False car in cherche si "e" est dans la liste d'element et non si il fait parti d'un mot de la liste
print ('ipsum' in list1)

    # Comparaison avec des nombres aléatoires
e = random.randint(0, 100)
f = random.randint(0, 100)
print(f'{e = }')
print(f'{f = }')

result = e == f
print(result)

result = e < f
print(result)

    # Est une expression
        # 1 + 1 -> 2 
        # (100 + 2) * 3 -> 102 + 3 -> 306
        # 1 + 1 > (100 + 2) * 3 -> False
        # random.randint(0, 100) 
        
    # Pas une expression    
        # print(100) 

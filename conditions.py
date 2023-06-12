import random

if True : 
    print("ce message s'affichera toujours")

if False :
    print("ce message ne s'affichera jamais")

number1 = random.randint(0, 10)
number2 = random.randint(0, 10)

print (f'{number1 = }')
print (f'{number2 = }')

    # Bloc if 1 :
if number1 < number2 :
    print("number1 est plus petit que number2")


    # Bloc Else : 
if number1 < number2 : # Si ...
    print("number1 est plus petit que number2")
else :  # Sinon ...
    print("la premiere condition n'est pas verifier")


    # Bloc Elif (= Else if) : 
if number1 < number2 : # Si ...
    print("number1 est plus petit que number2")
elif number1 > number2 :  # Ou si ...
    print("number1 est plus grande que number2")
else : # Sinon ...
    print("number1 et number2 sont egaux")


    # Réécriture du bloc Elif avec des If imbriqués :
if number1 < number2 :
    print("number1 est plus petit que number2")
else : 
    if number1 > number2 : 
        print("number1 est plus grande que number2")
    else :
        print("number1 et number2 sont egaux")


    # Opérateur booléens :

            # Négation : 
print(not True)
print(not False)

# table de verité de l'opérateur de négation
    #   A               not A
    #   True            False
    #   False           True


            
            # OU logique
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Table de vérité de l'opérateur OU logique :
    #     A                   B                A or B
    #   True                True        =>      True
    #   True                False       =>      True
    #   False               True        =>      True
    #   False               False       =>      False

    # pour retrouver la table, remplacez :
    # - A par "j'ai du cash"
    # - B par "j'ai ma CB"
    # - "A or B" par "puis-je faire mes courses ?"



            # ET logique
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Table de vérité de l'opérateur ET logique :
    #     A                   B                A and B
    #   True                True        =>      True
    #   True                False       =>      False
    #   False               True        =>      False
    #   False               False       =>      False

    # pour retrouver la table de ET, remplacez :
    # - A par "j'ai coupé l'electricité"
    # - B par "j'ai coupé l'eau"
    # - "A or B" par "puis-je partir 3 mois a l'étranger ?"


# Table de vérité de l'opérateur NAND (not and) :
    #     A                   B                A and B              Not (A and B)
    #   True                True        =>      True                False
    #   True                False       =>      False               True
    #   False               True        =>      False               True
    #   False               False       =>      False               True


# Utilisation de l'opérateur and pour voir si une variable est dans un interval de valeurs : 
age = random.randint (1, 99)
print(f'{age = }')

if age >= 12 and age <= 25 :
    print("l'age est compris entre 12 et 25 ans")
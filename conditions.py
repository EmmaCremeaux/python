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


            # OU exclusif (XOR) :
print(True ^ True)
print(True ^ False)
print(False ^ True)
print(False ^ False)

# Table de vérité de l'opérateur XOR :
    #     A                   B                A Xor B              
    #   True                True        =>      False                
    #   True                False       =>      True               
    #   False               True        =>      True               
    #   False               False       =>      False               





# Exo course (opérateur OU logique)
# Affichez : 
# je peux aller faire les courses si on a au moins un moyen de paiement.
# je ne peux pas si j'ai pas de moyen de paiement

has_cash = bool(random.randint(0, 1))
has_cb = bool(random.randint(0, 1))

print(f'{has_cash = }')
print(f'{has_cb = }')

if has_cash or has_cb:
    print("je peux allez faire mes courses")
else :
    print("je ne peux pas allez faire mes courses")


# Exo course (opérateur ET logique)
# Affichez : 
# je peux aller faire les courses si on a au moins un moyen de paiement.
# je ne peux pas si j'ai pas de moyen de paiement

has_cash = bool(random.randint(0, 1))
has_cb = bool(random.randint(0, 1))

print(f'{has_cash = }')
print(f'{has_cb = }')

if not has_cash and not has_cb :
    print("je ne peux pas allez faire mes courses")
else :
    print("je peux allez faire mes courses")



# Exo combinaison d'opérateur AND et OR :

has_score = bool(random.randint(0, 1))
has_level = bool(random.randint(0, 1))
has_vip = bool(random.randint(0, 1))

print(has_level)
print(has_score)
print(has_vip)

if (has_score and has_level) or has_vip : # Mettre les parenthèses aidera à empêcher les bugs
    print("tu peux avoir ton armure")
else :
    print("tu ne peux pas avoir ton armure")



# Exo carte de réduction
# Déterminez la carte de réduction auquelle le voyageur a droit : 
    # - entre 0 et 11 ans (inclus), gratuit
    # - entre 12 et 25 ans (inclus), reduc 50%
    # - entre 26 et 64 ans (inclus), reduc 10%
    # - au dela de 65 ans (inclus), reduc 50%

age = random.randint(0, 99)
print(age)

if 12 <= age <= 25 or age >= 65 : 
    print("reduc 50%")
elif 0 <= age <= 11 :
    print("gratuit")
else : 
    print("reduc 10%")

# Ou methode plus facilement changeable : 

if 12 <= age <= 25 : 
    print("reduc 50%")
elif age >= 65 : 
    print("reduc 50%")
elif 0 <= age <= 11 :
    print("gratuit")
else : 
    print("reduc 10%")

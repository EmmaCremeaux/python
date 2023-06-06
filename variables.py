#nombre entier, integer:
number1 = 123
number1= 42
print (number1)

#nombre a virgule flottante, float:
number2= 3.14
number2= 2.71
print(number2)

#chaine de caractères, string:
text1= "foo bar baz"
print(text1)

text2= "foo bar baz"
print(text2)

#booléen, boolean:
python_is_cool = True
python_is_boring = False

print(python_is_cool)
print(python_is_boring)

#Valeur nulle, null:
accepted_terms = None
print(accepted_terms)

#type de données:
print(type(number1))
print(type(number2))
print(type(text1))
print(type(python_is_cool))
print(type(accepted_terms))

#vérification du type de données: 
print(type(number1) is int)
print(type(number1) is str)
print(type(number2) is float)
print(type(number2) is int)
print(type(text1) is int)
print(type(text1) is str)
print(type(python_is_cool) is bool)
print(type(accepted_terms) is bool)

#transtypage int-> float: 
print(type(float(number1)))
print(float(number1))

#transtypage int-> bool: 
print(type(bool(number1)))
print(bool(number1))

#transtypage float-> int: 
print(type(int(number2)))
print(int(number2))

#converti en booléen, la valeur 0 donne False:
number3= 0
print(bool(number3))

# transtypage str -> int:
#génère une erreur :
# print(type(int(text1)))

#il ne peut pas y avoir autre chose qu'un nombre dans la chaine de caractère si on veux la convertir en 'int': 
text3= "123456789"
print((int(text3)))

# les fonctions de transtypage : 
# str() convertit vers une chaine de caractere
# int() convertit vers entier
# bool() convertit vers un bouléen
# float() convertit vers un nombre a virgule

#chaine de caractère, string : 
#cette notation permet d'utiliser des sauts de ligne : 
text4 = """<div>
    <h1>Titre de premier niveau</h1>
</div>
"""

# \n est equivalent a un saut de ligne
# \t est equivalent a une tabulation
text5 = "<div>\n\t<h1>Titre de premier niveau</h1>\n</div>\n"

print(text4)
print(text5)

text6 = "Foo\"Bar\" Baz"
print(text6)

#permutez les deux variables a et b en utilisant l'opérateur d'affectation et le nom des variables
a = 123
b = 42

# permutation des valeurs à l'aide de la méthode pythonique :
b, a = a, b

# permutation des valeurs à l'aide d'une variable temporaire : 
c = a 
a = b 
b = c

# permutayion des valeurs à l'aide d'opérations arithmétiques
a = a + b
b = a - b
a = a - b


print(a)
print(b)

# addition de float : 
print(0.1 + 0.1 +0.1 ) 
# ca affiche 0.30000000000000004 au lieu de 0.3
import decimal
from decimal import Decimal 

#affiche correctement 0.3
print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1"))

#Ne fonctionne pas pour additionner les float : 
#affiche "0.10.10.1" : 
print ("0.1" + "0.1" + "0.1")

# arrondi des floats
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
print(Decimal("0.05").quantize(Decimal("1"))) # = 0
print(Decimal("0.15").quantize(Decimal("0.1"))) # = 0.2

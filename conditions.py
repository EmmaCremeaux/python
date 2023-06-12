import random

if True : 
    print("ce message s'affichera toujours")

if False :
    print("ce message ne s'affichera jamais")

number1 = random.randint(0, 10)
number2 = random.randint(0, 10)

print (f'{number1 = }')
print (f'{number2 = }')

if number1 < number2:
    print("number1 est plus petit que number2")
else :
    print("number1 est plus grand que number2")
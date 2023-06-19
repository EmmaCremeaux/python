text1 = "lorem"
text2 = "ipsum"

# Concaténation
text3 = text1 + " " + text2
print(text3)

# Interpolation avec une f-string
text3 = f"{text1} {text2}" # l'espace est valide
print(text3)

mails = 52
text4 = "vous avez " + str(mails) + " non lus"  
# Bien indiquer que les mails doivent etre considéré comme une str pour que la concaténation fonctionne
# Il ne peut pas y avoir de mélange de type dans une concaténation
print(text4)


# Répétition de texte
text5 = "foo " * 3
print(text5)

# Affichage de valeurs arrondies mais sans arrondir la variable en int
number1 = 10 / 3
text6 = f"10 / 3 est a peu près {number1:.2f}"
print(text6)

# Les fonctions associés aux strings
text7 = "fou bar baz foo" # les espaces sont comptés
print(len(text7))

# Compter des mots
print(text7.count('foo'))

# Retrouve l'emplacement d'un mot
position = text7.find('foo')
print(position)

# Pour trouver l'occurence suivante, il faut chercher une position plus loin
print(text7.find('foo', position + 1))

# si le mot est absent, la fonction renvoie -1
position = text7.find('lorem')
print(position)

# Remplacement de mots
text7 = text7.replace('foo', 'lorem')
print(text7)

# Split & join
list1 = text7.split(' ')
print(list1)

text8 = " ".join(list1)
print(text8)

# Documenter une fonction : 

def ouiNon(value) : 
    """Cette fonction renvoie : 
    - "oui" si le parametre passé est True
    - "non" si le parametre passé est False
    - "" dans les autres cas."""

    if value == True : 
        return "oui"
    elif value == False : 
        return "non"

    return ""

help(ouiNon)
// exo 6.15
// Trouvez la chaîne de caractères la plus longue dans une liste.
// Affichez son index, sa valeur et sa longueur.
//
// ATTENTION : ne pas utiliser la fonction list.index()
// ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

// réponse 6.15 
let longueur = 0;
let valeur = '';
let index = null;

            // avec une boucle for :

for (let i = 0; i < my_list.length; i++) {
    // console.log(`${my_list[i]} est à l'index ${i} et a une longueur est de ${my_list[i].length}`);
    // console.log(' ')
    if (my_list[i].length > longueur) {
        longueur = my_list[i].length;
        valeur = my_list[i];
        index = i;
    }
}
console.log(`le mot le plus long est "${valeur}" est à l'index ${index} et a une longueur de ${longueur}.`);
            
            // boucle foreach qui permet de récupérer les valeurs mais pas l'index : 

let i = 0;
longueur = 0;
valeur = '';
index = null;

for (let word of my_list) {
    // console.log(i, word, word.length);
    if (word.length > longueur) {
        longueur = word.length;
        valeur = word;
        index = i;
    }
    i++
}
console.log(`le mot le plus long est "${valeur}" est à l'index ${index} et a une longueur de ${longueur}.`);
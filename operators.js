console.log("hello JS")
let number1 = 123;
let text1 = "123";

//Comparaison d'Egalité
console.log(number1 == text1);
// renvoie true

//Comparaison d'identité
console.log(number1 === text1);
//renvoie false

//Opérateur d'incrémentation
console.log(number1);

//number1 = number1 + 1
//number1 += 1
number1++;
//Attention l'incrémentation se fait aprés l'affichage
console.log(number1++);
console.log(number1);
//Solution pour que l'incrémentation se fait avant 
console.log(++number1);

//number1 = number1 - 1
//number1 -= 1
number1--;
console.log(number1);

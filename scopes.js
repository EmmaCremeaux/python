for (let i = 0; i < 10; i++) {
    console.log(i);
}

// si la variable i a été définie avec le mot clé let, elle n'est accessible que 
// si elle a été definie dans le même scope ou un scope exterieur
console.log(i);


for (var i = 0; i < 10; i++) {
    console.log(i);
}

// si la variable i a été définie avec le mot clé var, elle est accessible même
// si elle a été definie dans un scope intérieur
console.log(i)


function myFunc1() {
    var myVar1 = 123;
};

myFunc1();

// Même si la variable myVar1 est déclarée avec le mot clé var, 
// comme elle est déclérée à l'intérieur d'une fonction, 
// elle n'est pas accessible depuis un scope exterieur.
// console.log(myVar1);

// var transforme en limousine que les fonctions.
// let transforme en limousine tout les scopes avec accolade (boucle, if, function etc).


// Closure

function multNFactory(n) {
    return function multN(x) {
        return x * n;
    }
};

mult3 = multNFactory(3);

for (let i = 0; i < 3; i++) {
    console.log(mult3(i))
}

mult54 = multNFactory(54);

for (let i = 0; i < 3; i++) {
    console.log(mult54(i))
}


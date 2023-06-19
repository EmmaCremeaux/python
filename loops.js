// boucle for classique : 
for (let i = 0; i < 10; i++) {
    console.log("i = " + i)
};

// boucle à rebours : 
for (let i = 10; i > 0; i--) {
    console.log("i = " + i)
};

//boucle foreach
let users = ['foo', 'bar', 'baz'];
// le mot clé "of" en javascript equivaut a "in" en python
for (let user of users) {
    console.log(user)
};

// ici le mot clé "in" n'affiche que les index
for (let i in users) {
    let user = users[i] // pour avoir les user in doit créer une variable intermédiaire
    console.log(`i = ${i}, user = ${user}`);
};

// méthode forEach (asynchrone)
users.forEach(
    function(user, i, list) {
        console.log(`i = ${i}, user = ${user}`);
    }
);

// syntaxe alternative
users.forEach(
    (user, i, list) => console.log(`i = ${i}, user = ${user}`)
);


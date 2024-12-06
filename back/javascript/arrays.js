// How to create an array

// 1. New Array() or Array()

const fruits = Array('apple', 'banana', 'orange')
console.log(fruits)

const numbers = Array(1, 2, 3, 4, 5)
console.log(numbers)


// 2. Array literal syntax
const oneNumber = [4]
console.log(oneNumber)

// Mutabilidad 
const frutas = ["banana", "pera", "manzana"];
frutas.push("watermelon"); 
console.log(frutas);

// Inmutabilidad

const newFruits = fruits.concat(['grape', 'kiwi'])
console.log(newFruits)
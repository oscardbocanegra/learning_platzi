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

// metodos que iteran sobre un array

// FIlter
const number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
const evenNumbers = number.filter(num => num % 2 === 0)

console.log(number)
console.log(evenNumbers)


// Reduce

const numberReduce = [1, 2, 3, 4, 5]
const sum = numberReduce.reduce((accumulator, currentValue) => accumulator + currentValue, 0)

console.log(numberReduce)
console.log(sum)

// Slice()

const animals = ["Dog", "Camel", "Cat", "Fish", "Fox", "Duck"]

console.log(animals.slice(2))
console.log(animals.slice(2, 4))
console.log(animals.slice(1, 6))
console.log(animals.slice(-3))
console.log(animals.slice(2, -1))
console.log(animals.slice())
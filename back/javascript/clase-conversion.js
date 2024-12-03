// conversion de tipos en js de manera explicita

const string = '42'
const integer = parseInt(string)
console.log(integer)
console.log(typeof integer)

const stringDecimal = '3.14'
const float = parseFloat(stringDecimal)
console.log(float)
console.log(typeof float)

// operadores de comparacion
console.log("Operadores de comparacion")
const a = 10 
const b = 20
const c = "10"

console.log(a == b)
console.log(a === c)
console.log(a != b)
console.log(a !== c)
console.log(a > b)
console.log(a <= b)
console.log(a > c)
/**
 * Demonstrates array destructuring by extracting elements from an array
 * into individual variables.
 * 
 * Example:
 * let fruits = ['Apple', 'Banana'];
 * let [a, b] = fruits;
 * console.log(a, fruits[1]); // Output: Apple Banana
 */

/**
 * Demonstrates object destructuring by extracting properties from an object
 * into individual variables.
 * 
 * Example:
 * let user = { username: 'Oscar', age: 34 };
 * let { username, age } = user;
 * console.log(username, user.age); // Output: Oscar 34
 */
// arrys destructuring

let fruits = ['Apple', 'Banana'];
let [a, b] = fruits;
console.log(a, fruits[1]); // Apple Banana

// Object destructuring
let user = { username: 'Oscar', age: 34 };
let { username, age } = user;
console.log(username, user.age); // Oscar 34

// spread operator

let person = { name: 'Oscar', age: 21 };
let country = 'CO';

let data = { ...person, country };
console.log(data); // { name: 'Oscar', age: 21, country: 'CO' }

// Rest operator

function sum(num, ...values) {
    console.log(num); // 1
    console.log(values); // [2, 3, 4, 5]
    return num + values.length;
}   

console.log(sum(1, 2, 3, 4, 5)); // 5
console.log(sum(1)); // 1


let json1 = { name: 'Bigotes', food: "Pollito" };
let json2 = { name: 'Oscar', age: 21, country: 'CO' };

export function solution(json1, json2) {
    // Tu código aquí 👈
     let data = { ...json1, ...json2 }
     console.log(data); // { name: 'Oscar', age: 21, country: 'CO' }
   }


   
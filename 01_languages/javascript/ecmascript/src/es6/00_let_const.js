/**
 * Demonstrates the behavior of variable declarations using `var`, `let`, and `const` in JavaScript.
 * 
 * - `var` has function scope and allows reassignment.
 * - `let` has block scope and allows reassignment.
 * - `const` has block scope and does not allow reassignment.
 * 
 * The code also includes a function to showcase the scoping rules of `var`, `let`, and `const`.
 */

/**
 * Reassigns a variable declared with `var` and logs the result.
 * Demonstrates that `var` allows reassignment.
 */
var lastName = 'David';
lastName = 'Bocanegra';
console.log(lastName); // Logs: Bocanegra

/**
 * Reassigns a variable declared with `let` and logs the result.
 * Demonstrates that `let` allows reassignment within its block scope.
 */
let fruit = 'Apple';
fruit = 'Kiwi';
console.log(fruit); // Logs: Kiwi

/**
 * Attempts to reassign a variable declared with `const` and logs the result.
 * Demonstrates that `const` does not allow reassignment.
 * 
 * @throws {TypeError} Assignment to constant variable.
 */
const animal = 'Dog';
animal = 'Cat'; // Error: Assignment to constant variable.
console.log(animal); // Error: Assignment to constant variable

/**
 * Demonstrates the scoping rules of `var`, `let`, and `const` within a function.
 * 
 * - `var` is function-scoped and accessible outside the block.
 * - `let` and `const` are block-scoped and not accessible outside the block.
 * 
 * @function
 * @throws {ReferenceError} If attempting to access `let` or `const` variables outside their block scope.
 */
const fruits = () => {
    if (true) {
        var fruit1 = 'Apple'; // function scope
        let fruit2 = 'Banana'; // block scope
        const fruit3 = 'Cherry'; // block scope
    }
    console.log(fruit1); // Logs: Apple
    console.log(fruit2); // Error: fruit2 is not defined
    console.log(fruit3); // Error: fruit3 is not defined
};

fruits();
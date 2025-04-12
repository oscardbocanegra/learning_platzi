/**
 * Creates a new user with default parameters if no arguments are provided.
 * 
 * This function uses the old ES5 approach to set default values by using the `||` operator.
 * If a value is falsy (e.g., `undefined`, `null`, `false`, `0`, or an empty string), 
 * the default value will be assigned.
 * 
 * @param {string} [name='Oscar'] - The name of the user. Defaults to 'Oscar' if not provided.
 * @param {number} [age=34] - The age of the user. Defaults to 34 if not provided.
 * @param {string} [country='MX'] - The country of the user. Defaults to 'MX' if not provided.
 */
function newUser(name, age, country) {
    // Function implementation
}

/**
 * Creates a new admin with default parameters using ES6 default parameter syntax.
 * 
 * This function demonstrates the modern ES6 approach to setting default values directly 
 * in the function signature. Unlike the `||` operator approach, this method is more 
 * concise and does not override falsy values like `0` or an empty string.
 * 
 * @param {string} [name='Oscar'] - The name of the admin. Defaults to 'Oscar' if not provided.
 * @param {number} [age=20] - The age of the admin. Defaults to 20 if not provided.
 * @param {string} [country='MX'] - The country of the admin. Defaults to 'MX' if not provided.
 */
function newAdmin(name = 'Oscar', age = 20, country = 'MX') {
    // Function implementation
}

/**
 * Key Difference Between `newUser` and `newAdmin`:
 * 
 * - `newUser` uses the ES5 approach with the `||` operator to assign default values. 
 *   This method can unintentionally override falsy values like `0` or an empty string.
 * - `newAdmin` uses the ES6 default parameter syntax, which is more robust and does not 
 *   override falsy values unless explicitly set to `undefined`.
 */


function newUser (name, age, country){
    var name = name || 'Oscar';
    var age = age || 34;
    var country = country || 'MX';
    console.log(name, age, country);
}

newUser(); // Oscar 34 MX
newUser('David', 21, 'CO'); // Ricardo 23 CO


function newAdmin (name = 'Oscar', age = 20, country = 'MX'){
    console.log(name, age, country);
}

newAdmin(); // Oscar 20 MX
newAdmin('Ricardo', 23, 'CO'); // Ricardo 23 CO


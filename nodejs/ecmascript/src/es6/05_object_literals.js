/**
 * Creates a new user object with the provided details.
 * 
 * @function newUser
 * @param {string} name - The name of the user.
 * @param {number} age - The age of the user.
 * @param {string} country - The country of the user.
 * @param {string} uId - The unique identifier for the user.
 * @returns {Object} A new user object containing the provided details.
 * @property {string} name - The name of the user.
 * @property {number} age - The age of the user.
 * @property {string} country - The country of the user.
 * @property {string} id - The unique identifier for the user.
 */
// enahced object literals

function newUser(name, age, country, uId){
    return {
        name,
        age,
        country,
        id: uId
    }
}

console.log(newUser('Oscar', 21, 'COL'));
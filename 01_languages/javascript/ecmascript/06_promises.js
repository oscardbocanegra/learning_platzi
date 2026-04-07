/**
 * Creates a new Promise that resolves or rejects based on a condition.
 *
 * @function
 * @returns {Promise<string>} A promise that resolves with the string 'Hey!' 
 * if the condition is true, or rejects with the string 'Whoops!' if the condition is false.
 *
 * @example
 * anotherFunction()
 *   .then((response) => console.log(response)) // Logs 'Hey!' to the console
 *   .catch((error) => console.log(error)); // Logs 'Whoops!' if the promise is rejected
 */
const anotherFunction = () => {
  return new Promise((resolve, reject) => {
    if (true) {
      resolve('Hey!');
    } else {
      reject('Whoops!');
    }
  });
};  

anotherFunction()
  .then((response) => console.log(response)) // This will log 'Hey!' to the console
  .catch((error) => console.log(error)); // This will not be executed because the promise is resolved

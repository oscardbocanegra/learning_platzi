const words = ["javascript", "frontend", "backend", "developer", "programming"];
let chosenWord = "";
let attemptsLeft = 6;
let guessedLetters = [];
let wrongLetters = [];

const wordDisplay = document.getElementById("wordDisplay");
const attemptsDisplay = document.getElementById("attemptsLeft");
const wrongLettersDisplay = document.getElementById("wrongLetters span");
const messageDisplay = document.getElementById("message");
const letterInput = document.getElementById("letterInput");
const checkButton = document.getElementById("checkButton");
const resetButton = document.getElementById("resetButton");
const canvas = document.getElementById("hangmanCanvas");
const ctx = canvas.getContext("2d");

function chooseWord() {
  chosenWord = words[Math.floor(Math.random() * words.length)];
}

function displayWord() {
  const display = chosenWord
    .split("")
    .map((letter) => (guessedLetters.includes(letter) ? letter : "_"))
    .join(" ");
  wordDisplay.textContent = display;
}

function updateCanvas() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "black";

  // Base
  if (attemptsLeft <= 5) ctx.fillRect(10, 230, 180, 10);

  // Pole
  if (attemptsLeft <= 4) ctx.fillRect(50, 10, 10, 220);

  // Top bar
  if (attemptsLeft <= 3) ctx.fillRect(50, 10, 100, 10);

  // Rope
  if (attemptsLeft <= 2) ctx.fillRect(140, 20, 2, 20);

  // Head
  if (attemptsLeft <= 1) ctx.beginPath(), ctx.arc(141, 50, 15, 0, Math.PI * 2), ctx.stroke();

  // Body
  if (attemptsLeft <= 0) {
    ctx.fillRect(140, 65, 2, 50); // Body
    ctx.fillRect(140, 115, -20, 2); // Left Arm
    ctx.fillRect(140, 115, 20, 2); // Right Arm
    ctx.fillRect(140, 115, -20, 2); // Left Leg
    ctx.fillRect(140, 155, 20, 2); // Right Leg
  }
}

function checkLetter() {
  const letter = letterInput.value.toLowerCase();
  if (!letter || guessedLetters.includes(letter) || wrongLetters.includes(letter)) {
    messageDisplay.textContent = "Letra inválida o ya usada.";
    return;
  }

  messageDisplay.textContent = "";
  if (chosenWord.includes(letter)) {
    guessedLetters.push(letter);
  } else {
    wrongLetters.push(letter);
    attemptsLeft--;
  }

  attemptsDisplay.textContent = attemptsLeft;
  wrongLettersDisplay.textContent = wrongLetters.join(", ");
  displayWord();
  updateCanvas();

  if (!wordDisplay.textContent.includes("_")) {
    messageDisplay.textContent = "¡Felicidades! Ganaste 🎉";
    disableInput();
  } else if (attemptsLeft <= 0) {
    messageDisplay.textContent = `Perdiste. La palabra era "${chosenWord}".`;
    disableInput();
  }

  letterInput.value = "";
}

function disableInput() {
  letterInput.disabled = true;
  checkButton.disabled = true;
}

function resetGame() {
  attemptsLeft = 6;
  guessedLetters = [];
  wrongLetters = [];
  messageDisplay.textContent = "";
  letterInput.disabled = false;
  checkButton.disabled = false;
  chooseWord();
  displayWord();
  updateCanvas();
  attemptsDisplay.textContent = attemptsLeft;
  wrongLettersDisplay.textContent = "";
}

chooseWord();
displayWord();
updateCanvas();

checkButton.addEventListener("click", checkLetter);
resetButton.addEventListener("click", resetGame);

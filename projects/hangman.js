const themes = {
  animals: ["alligator", "ant", "bat", "bear", "beaver", "cat", "dog", "eagle", "elephant", "giraffe", "lion", "monkey", "panda", "penguin", "rabbit", "tiger", "wolf", "zebra"],
  food: ["apple", "banana", "carrot", "cheese", "cookie", "fries", "mango", "milk", "onion", "pizza", "salad", "sushi"],
  ice_cream: ["vanilla", "chocolate", "strawberry", "mint", "rockyroad", "butterpecan"],
  instruments: ["guitar", "piano", "drums", "violin", "flute", "saxophone"]
};

const hangmanArt = [
`  +---+
  |   |
      |
      |
      |
      |
=========`,
`  +---+
  |   |
  O   |
      |
      |
      |
=========`,
`  +---+
  |   |
  O   |
  |   |
      |
      |
=========`,
`  +---+
  |   |
  O   |
 /|   |
      |
      |
=========`,
`  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========`,
`  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========`,
`  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========`
];

let answer = "";
let guessedLetters = [];
let wrongGuesses = [];

function startGame() {
  const theme = document.getElementById("theme-select").value;
  const words = themes[theme];
  answer = words[Math.floor(Math.random() * words.length)];
  guessedLetters = [];
  wrongGuesses = [];
  document.getElementById("message").textContent = "";
  document.getElementById("wrong-letters").textContent = "";
  updateWordDisplay();
  updateHangman();
  createLetterButtons();
}

function updateWordDisplay() {
  const display = answer
    .split("")
    .map(letter => guessedLetters.includes(letter) ? letter : "_")
    .join(" ");
  document.getElementById("word-display").textContent = display;

  if (!display.includes("_")) {
    document.getElementById("message").textContent = "🎉 You won!";
    disableAllButtons();
  }
}

function updateHangman() {
  const wrongCount = wrongGuesses.length;
  document.getElementById("hangman-art").textContent = hangmanArt[wrongCount];
  document.getElementById("wrong-letters").textContent = wrongGuesses.join(", ");
  if (wrongCount >= hangmanArt.length - 1) {
    document.getElementById("message").textContent = `💀 You lost! The word was: ${answer} 💀`;
    disableAllButtons();
  }
}

function createLetterButtons() {
  const container = document.getElementById("letters");
  container.innerHTML = "";
  for (let i = 65; i <= 90; i++) {
    const letter = String.fromCharCode(i).toLowerCase();
    const button = document.createElement("button");
    button.textContent = letter;
    button.onclick = () => handleGuess(letter, button);
    container.appendChild(button);
  }
}

function handleGuess(letter, button) {
  button.disabled = true;
  if (answer.includes(letter)) {
    guessedLetters.push(letter);
    updateWordDisplay();
  } else {
    if (!wrongGuesses.includes(letter)) {
      wrongGuesses.push(letter);
      updateHangman();
    }
  }
}

function disableAllButtons() {
  document.querySelectorAll("#letters button").forEach(button => {
    button.disabled = true;
  });
}
# Wordle

A Python implementation of the popular word-guessing game Wordle. The player has six attempts to guess a hidden 5-letter word, with color-coded feedback given for each guess.

## Preview
<img width="375" height="525" alt="image" src="https://github.com/user-attachments/assets/4c6670a9-2a44-4a9e-9328-bb34e98507f8" />

## How to Play

- Guess the hidden **5-letter word** in 6 tries or less.
- Each guess must be a valid 5-letter word.
- After each guess, the color of the tiles will change to show how close your guess was to the word:
  - 🟩 **Green:** The letter is in the word and in the correct spot.
  - 🟨 **Yellow:** The letter is in the word but in the wrong spot.
  - ⬛ **Gray:** The letter is not in the word in any spot.

## How to Run the Game

To download and run this game locally on your machine:

**1. Clone the repository:**
   ```bash
   git clone [https://github.com/AnhThy3447/Wordle.git](https://github.com/AnhThy3447/Wordle.git)
   cd Wordle
   ```
**2. Run the application:**
   ```bash
   python app.py
   ```

## Credits & Acknowledgements

Word list dataset provided by [steve-kasica](https://github.com/steve-kasica) from the repository [wordle-words](https://github.com/steve-kasica/wordle-words).

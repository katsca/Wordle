# WORDLE
This is my simple attempt at recreating Wordle

## SET UP

1. Clone the repo:
    ```bash
    git clone https://github.com/katsca/Wordle.git
    cd Wordle
    ```

2. Create a virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate #Linux/macOS
    venv\scripts\activate #Windows

3. Install dependencies

    ```bash
    pip instsall -r requirements.txt
    ```

## Usage
To run the game
    ```bash
    python main.py
    ```

## Playing the game

### Controls
* To reset the game at any point press ESC
* Use alphanumeric keys to type the word and backspace to delete or press the keys on the keyboard
* Press enter to a guess
* Press left shift to switch from dark to light mode
* Window can be resized but only in the same aspect ratio - default is 600x800
### Rules
* Each guess must be a valid five-letter word.
* The color of a tile will change to show you how close your guess was.
    * If the tile turns green, the letter is in the word, and it is in the correct spot.
    * If the tile turns yellow, the letter is in the word, but it is not in the correct spot.
    * If the tile turns gray, the letter is not in the word.
* You have max 6 guesses before the solution is revealed
* Upon restarting a randomly new solution is generated from a list of valid five-letter words

### Images of the game





# Number Guessing Game

## Description
The Number Guessing Game is a simple command-line game where the player tries to guess a randomly generated number between 1 and 100. The game provides feedback on whether the guess is too high or too low, and indicates if the guess is close to the target number.

## Features
- Random number generation between 1 and 100
- User input for guesses
- Feedback on whether the guess is too high, too low, or close to the target number
- Keeps track of the number of attempts
- Congratulates the player when the correct number is guessed

## Getting Started

### Prerequisites
Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/zatovitch/number-guessing-game.git
    ```
2. Navigate to the project directory:
    ```sh
    cd number-guessing-game
    ```
3. (Optional) Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
To start the game, run the following command:
```sh
python src/game.py
```

### Running Tests
To ensure the game functions as expected, run the tests using:
```
python -m unittest discover -s tests
```

## Project Structure
```
number-guessing-game
├── src
│   ├── game.py
│   └── __init__.py
├── tests
│   └── test_game.py
├── requirements.txt
└── README.md
```

## Contributing
If you would like to contribute to the project, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
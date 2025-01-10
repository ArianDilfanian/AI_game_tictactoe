# Tic-Tac-Toe AI with GUI

This project is an advanced implementation of the classic Tic-Tac-Toe game. It features an AI opponent capable of playing at two difficulty levels (easy and hard) and includes a modern graphical user interface (GUI) built using Python's Pygame library.

---

## Features

- **Graphical User Interface**

  - Interactive and visually appealing GUI.
  - Dynamic buttons for choosing the player and difficulty levels.
  - Clear game board with responsive visuals.

- **AI Opponent**

  - **Easy Mode**: Includes randomness for less challenging gameplay.
  - **Hard Mode**: Implements the Minimax algorithm for optimal moves.

- **Customization**

  - Blue X (❌) and red O (⭕) for distinct player moves.
  - Adjustable game board and interface layout.

- **Replayability**

  - "Play Again" button to restart the game easily after completion.

---

## Project Structure

- ``: Core logic for the game, including the Minimax algorithm, board state evaluation, and utility functions.
- ``: The GUI implementation using Pygame.

---

## How to Run

1. **Prerequisites**:

   - Python 3.7+
   - Pygame library (Install using `pip install pygame`)

2. **Clone the Repository**:

   ```bash
   git clone https://github.com/ArianDilfanian/tictactoe-ai.git
   cd tictactoe-ai
   ```

3. **Run the Game**:

   ```bash
   python runner.py
   ```

4. Follow the on-screen instructions to choose your player and difficulty level, then enjoy the game!

---

## Controls and Gameplay

- Click the buttons to select your player (❌ or ⭕) and difficulty level.
- The game board consists of a 3x3 grid where you can place your move by clicking on an empty cell.
- The AI will automatically make its move when it's the computer's turn.
- The game ends with a win, loss, or tie, and you can replay with the "Play Again" button.

---

## Technical Details

### AI Implementation

- The AI uses the **Minimax Algorithm** for decision-making:
  - Evaluates all possible moves to determine the optimal choice.
  - Depth limitation for Easy Mode ensures reduced difficulty.

### Pygame Features

- Dynamic button rendering for interactivity.
- Responsive board layout that adapts to user input.
- Customizable colors for X and O.

---

## Future Improvements

- Add support for multiplayer mode.
- Enhance GUI with animations and sound effects.
- Optimize AI performance for larger grids.
- Implement a scoring system to track wins and losses over multiple rounds.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- **CS50 Course**: Inspiration for implementing the Minimax algorithm.
- **Pygame Community**: For providing excellent documentation and resources.

---

## Contributing

Contributions are welcome! If you’d like to improve this project, feel free to fork the repository and submit a pull request.

---

Enjoy playing Tic-Tac-Toe with an intelligent AI! 🎮


"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = sum(row.count(X) for row in board)
    countO = sum(row.count(O) for row in board)
    return O if countX > countO else X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    i, j = action
    board_copy = copy.deepcopy(board)
    board_copy[i][j] = player(board)
    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for line in board + list(zip(*board)):  # Check rows and columns
        if line[0] == line[1] == line[2] and line[0] is not None:
            return line[0]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell is not None for row in board for cell in row)

def utility(board):
    """
    Returns 1 if X has won, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0

current_minimax = None

def set_difficulty(mode):
    """
    Sets the current difficulty mode and updates the minimax function.
    """
    global current_minimax
    current_minimax = difficulty(mode)

# Define the difficulty levels
def difficulty(mode):
    def max_value(board, depth=2):
        if terminal(board):
            return utility(board)
        if depth == 0 and mode == "easy":
            return 0
        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action), depth - 1))
        return v

    def min_value(board, depth=2):
        if terminal(board):
            return utility(board)
        if depth == 0 and mode == "easy":
            return 0
        v = math.inf
        for action in actions(board):
            v = min(v, max_value(result(board, action), depth - 1))
        return v

    def minimax(board):
        if terminal(board):
            return None
        if mode == "easy" and random.random() < 0.3:
            return random.choice(list(actions(board)))
        plays = [
            (min_value(result(board, action), depth=2 if mode == "hard" else 1), action)
            if player(board) == X else
            (max_value(result(board, action), depth=2 if mode == "hard" else 1), action)
            for action in actions(board)
        ]
        return sorted(plays, key=lambda x: x[0], reverse=(player(board) == X))[0][1]

    return minimax

# Default mode
set_difficulty("hard")

def minimax(board):
    """
    Delegates to the current difficulty's minimax function.
    """
    if current_minimax is None:
        raise Exception("AI difficulty is not set. Call set_difficulty(mode) first.")
    return current_minimax(board)




            


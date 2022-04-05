"""
Tic Tac Toe Player
"""

import math
import copy

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
    compterx = 0
    compter0 = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row] [col] == X:
                compterx += 1
            elif board[row] [col] ==O:
                compter0 += 1
    return X if compterx == compter0 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = set()

    for row in range(0, len(board)):
        for col in range(0, len(board[0])):
            if board[row][col] == EMPTY:
                possible.add((row, col))

    return possible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (x, y) = action
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
        raise IndexError()
    tableau_action = [row[:] for row in board]
    tableau_action[x][y] = player(board)
    return tableau_action


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRows(board, X) or checkCol(board, X) or checktop(board, X) or checkbottom(board, X):
        return X
    elif checkRows(board, O) or checkCol(board, O) or checktop(board, O) or checkbottom(board, O):
        return O
    else:
        return None
def checkRows(board, player):
    for row in range(len(board)):
        compter = 0
        for col in range (len(board[0])):
            if board [row] [col] == player:
                compter += 1
            if compter == len(board[0]):
                return True
    return False

def checkCol(board, player):
    for col in range(len(board[0])):
        compter = 0
        for row in range (len(board)):
            if board [row] [col] == player:
                compter += 1
            if compter == len(board):
                return True
    return False

def checktop(board, player):
    compter = 0
    for row in range(len(board)):
        for col in range (len(board[0])):
            if row == col and board  [row] [col] == player:
                compter += 1

    return compter == len(board[0])


def checkbottom(board, player):
    compter = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (len(board) - row - 1) == col and board [row] [col] == player:
                compter += 1
    return compter == len(board[0])

def tie(board):
    comptervide = (len(board) * len(board[0]))
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] is EMPTY:
                comptervide -= 1
    return comptervide == 0


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False
    #return True if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None) else False # noqa E501


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    # Check how to handle exception when a non terminal board is received.


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move
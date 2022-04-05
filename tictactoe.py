"""
Tic Tac Toe Player
"""

import math

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
    posiblite = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board [row] [col] == EMPTY:
                posiblite.add(row, col)
    return posiblite




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (x, y) = action
    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
        raise IndexError()
    tableau_action = [row[:] for row in board]
    tableau_action[x] [y] = player(board)
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

def liste(board):
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
    if winner(board) or liste(board):
        return True
    else:
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return  1
    elif winner(board) == O:
        return  -1
    else:
        return  0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        arr = []
        for action in actions():
            arr.append([min_value(result(board, action)), action])
        return sorted(arr, key=lambda X: X[0], reverse=True)[0][1]
    elif player(board) == O:
        arr = []
        for action in actions(board):
            arr.append([max_value(result(board, action)), action])
        return sorted(arr, key=lambda X: X[0])[0][1]
def max_value(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max (v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = min (v, max_value(result(board, action)))
    return v

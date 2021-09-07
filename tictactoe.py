"""
Tic Tac Toe Player
"""

from helpers import helpers
import math
import numpy as np
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for num in row:
            if num == X:
                x_count += 1
            elif num == O:
                o_count += 1
    return O if x_count > o_count else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid Action!!!")

    b2 = copy.deepcopy(board)
    b2[action[0]][action[1]] = player(board)

    return b2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    isTerminal = terminal(board)

    if isTerminal != False and isTerminal != True:
        return isTerminal[1]
    elif isTerminal == False:
        return False
    return None


def terminal(board):
    for newBoard in [board, np.transpose(board)]:
        result = helpers.checkRows(newBoard)
        if result:
            return result
        diag_result = helpers.checkDiagonals(board)
        if diag_result:
            return diag_result
    return helpers.checkTie(board)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1

    elif winner(board) == O:
        return -1

    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    Max = float("-inf")
    Min = float("inf")

    if player(board) == X:
        return Max_Value(board, Max, Min)[1]
    else:
        return Min_Value(board, Max, Min)[1]


def Max_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None]
    v = float("-inf")
    for action in actions(board):
        test = Min_Value(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        if test > v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move]


def Min_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None]
    v = float("inf")
    for action in actions(board):
        test = Max_Value(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move]

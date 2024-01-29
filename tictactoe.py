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
    countX = 0
    countO = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                countX +=1
            elif board[i][j] == O:
                countO += 1

    if countX == countO:
        return X
    else:
        return O



    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                possible_actions.add((i,j))

    return possible_actions
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    xnumber = 0
    onumber = 0
    xtrue = True
    if board[action[0]][action[1]] != EMPTY:
        raise Exception
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                xnumber += 1
            elif board[i][j] == O:
                onumber += 1
    if xnumber > onumber:
        xtrue = False
    newboard = copy.deepcopy(board)
    if xtrue == True:
        newboard[action[0]][action[1]] = X
    else:
        newboard[action[0]][action[1]] = O
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    """
        Checks each row or column linearly if a person won
    """
    for i in range(3):
        if (board[i][0] == X and board[i][1] == X and board[i][2] == X) or (board[0][i] == X and board[1][i] == X and board[2][i] == X):
            return X
        elif (board[i][0] == O and board[i][1] == O and board[i][2] == O) or (board[0][i] == O and board[1][i] == O and board[2][i] == O):
            return O
    """
    Checks diagonally if a person won
    """
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X) or (board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return X
    elif (board[0][0] == O and board[1][1] == O and board[2][2] == O) or (board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    isDraw = True
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                return False
    if isDraw == True:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) is True:
        if winner(board) is X:
            return 1
        elif winner(board) is O:
            return -1
        else:
            return 0
    return None


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    bestaction = None
    if player(board) == X:
        value = -math.inf
        for action in actions(board):
            mv = minval(result(board, action))
            if mv > value:
                value = mv
                bestaction = action

    if player(board) == O:
        value = math.inf
        for action in actions(board):
            xv = maxval(result(board, action))
            if xv < value:
                value = xv
                bestaction = action
    return bestaction           # raise NotImplementedError


def maxval(board):
    if terminal(board):
        return utility(board)
    value = -math.inf
    for action in actions(board):
        value = max(value, minval(result(board, action)))
    return value


def minval(board):
    if terminal(board):
        return utility(board)
    value = math.inf
    for action in actions(board):
        value = min(value, maxval(result(board, action)))
    return value



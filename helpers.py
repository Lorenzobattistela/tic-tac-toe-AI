EMPTY = None


class helpers:
    def checkRows(board):
        for row in board:
            if len(set(row)) == 1 and EMPTY not in set(row):
                return True, row[0]
        return False

    def checkDiagonals(board):
        if len(set([board[i][i] for i in range(len(board))])) == 1 and EMPTY not in set(
            [board[i][i] for i in range(len(board))]
        ):
            return True, board[0][0]
        if len(
            set([board[i][len(board) - i - 1] for i in range(len(board))])
        ) == 1 and EMPTY not in set(
            [board[i][len(board) - i - 1] for i in range(len(board))]
        ):
            return True, board[0][len(board) - 1]
        return False

    def checkTie(board):
        checked = []
        for row in board:
            for num in row:
                checked.append(num)
        if EMPTY in checked:
            return False
        else:
            return True

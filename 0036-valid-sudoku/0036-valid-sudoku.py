class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in range(9):
            row_dict = set()
            for i in range(9):
                if board[row][i] in row_dict and board[row][i] != ".":
                    return False
                else:
                    row_dict.add(board[row][i])
        
        for col in range(9):
            col_dict = set()
            for j in range(9):
                if board[j][col] in col_dict and board[j][col] != ".":
                    return False
                else:
                    col_dict.add(board[j][col])
        
        a = [0,3,6]
        m = [[x,y] for x in a for y in a]

        for x in m:
            grid_dict = set()
            for row in range(x[0], x[0] + 3):
                for col in range(x[1], x[1] + 3):
                    if board[row][col] in grid_dict and board[row][col] != ".":
                        return False
                    else:
                        grid_dict.add(board[row][col])

        return True
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix),  len(matrix[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        starts = list()
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    starts.append((r,c))
        
        while starts:
            r, c = starts.pop()
            for c_n in range(COLS):
                matrix[r][c_n] = 0
            for r_n in range(ROWS):
                matrix[r_n][c] = 0
        
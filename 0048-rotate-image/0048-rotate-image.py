class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # [1,2],[3,4] -> [3, 1][4,2]
        # vertical flip:
        n = len(matrix)
        for i in range(n//2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
        
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i] , matrix[i][j]
        
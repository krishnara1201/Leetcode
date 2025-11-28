class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        res = ""
        matrix = [[""] * n for _ in range(numRows)]
        
        i, down, right = 0, 0, 0

        while i < n:
            while down < numRows and i < n:
                matrix[down][right] += s[i]
                i += 1
                down += 1
            down -= 1
            while down > 1 and i < n:
                down -= 1
                right += 1
                matrix[down][right] += s[i]
                i += 1
            down -= 1
            right += 1

        res = ""
        for r in range(numRows):
            res += "".join(matrix[r])

        return res
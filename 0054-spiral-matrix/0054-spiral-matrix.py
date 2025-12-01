class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        visit = set()
        res = []
        direction = "right"

        def dfs(r,c):
            nonlocal res, direction
            print(r,c,direction)

            if ((r,c) in visit or 
            r < 0 or r >= rows or
            c < 0 or c >= cols):
                if direction == "right":
                    direction = "down"
                elif direction == "down":
                    direction = "left"
                elif direction == "left":
                    direction = "up"
                else:
                    direction = "right"
                
            else:
                res.append(matrix[r][c])
                visit.add((r,c))
                for _ in range(2):
                    if direction == "up":
                        dfs(r-1,c)
                    if direction == "right":
                        dfs(r,c+1)
                    if direction == "down":
                        dfs(r+1,c)
                    if direction == "left":
                        dfs(r,c-1)
                
        dfs(0,0)
        return res


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        steps = 0
        q = deque([entrance])
        maze[entrance[0]][entrance[1]] = '+'

        while q:
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()

                if (((r == ROWS - 1) or (r == 0) or
                    (c == COLS - 1) or (c == 0)) and 
                    [r,c] != entrance):
                    return steps
                

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if ((0 <= nr < ROWS) and 
                        (0 <= nc < COLS) and 
                        maze[nr][nc] != '+'):
                        maze[nr][nc] = '+'
                        q.append([nr,nc])
            steps += 1
        
        return -1


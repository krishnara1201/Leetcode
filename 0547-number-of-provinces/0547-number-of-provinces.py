class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS, COLS = len(isConnected), len(isConnected[0])
        adj_set = collections.defaultdict(list)
        for r in range(ROWS):
            adj_set[r] = []
            for c in range(COLS):
                if isConnected[r][c] and r != c:
                    adj_set[r].append(c)
        
        # print(adj_set)
        visit = set()
        def dfs(key):
            visit.add(key)
            # print(adj_set)
            while adj_set[key]:
                nei = adj_set[key].pop()
                dfs(nei)

            return 

        count = 0
        for key in adj_set.keys():
            if adj_set[key]:
                count += 1
                dfs(key)
            if key not in visit:
                visit.add(key)
                count += 1

        return count 
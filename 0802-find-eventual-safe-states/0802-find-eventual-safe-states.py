class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        res = set()
        path = set()
        
        def dfs(node):
            if node in path:
                return False
            if node in res:
                return True

            for nei in graph[node]:
                path.add(node)
                if not dfs(nei):
                    return False
                path.remove(node)
            
            res.add(node)
            return True

        for i in range(len(graph)):
            if i not in res:
                dfs(i)
        return sorted(list(res))

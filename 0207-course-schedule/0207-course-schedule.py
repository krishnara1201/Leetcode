class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqset = {i:[] for i in range(numCourses)}

        for a,b in prerequisites:
            reqset[a].append(b)

        vis = [False] * numCourses
        path = [False] * numCourses

        def dfs(course):
            vis[course] = path[course] = True
            
            for c in reqset[course]:
                if not vis[c]:
                    if dfs(c): return True
                elif path[c]: return True
            
            path[course] = False
            return False

        
        for i in reqset.keys():
            if not vis[i]:
                if dfs(i): 
                    return False

        return True
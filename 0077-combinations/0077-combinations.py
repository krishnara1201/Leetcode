class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i,stack):
            if len(stack) == k:
                res.append(stack.copy())
            elif i > n:
                return 
            else:
                stack.append(i)
                dfs(i+1, stack)
                stack.pop()
                dfs(i+1, stack)

        dfs(1, [])
        return res
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = []
        res = []
        n = len(candidates)
        def dfs(cur_sum, i, stack):
            if cur_sum == target:
                res.append(stack.copy())
            elif cur_sum > target or i == n:
                return
            else:
                stack.append(candidates[i])
                dfs(cur_sum + candidates[i], i, stack)
                stack.pop()
                dfs(cur_sum, i + 1, stack)

        dfs(0, 0, stack)
        return res
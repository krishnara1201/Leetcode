class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, stack = [], []
        n = len(nums)
        count = collections.Counter(nums)

        def dfs():
            if len(stack) == n:
                res.append(stack[::])
            
            for num in count:
                if count[num] > 0:
                    count[num] -= 1
                    stack.append(num)
                    dfs()
                    stack.pop()
                    count[num] += 1
        
        dfs()
        return res
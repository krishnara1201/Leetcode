class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf")] * n
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            if nums[i] + i >= n - 1:
                dp[i] = 1
            else:
                for j in range(nums[i] + 1):
                    if i + j < n:
                        dp[i] = min(dp[i], 1 + dp[i+j])
                    else:
                        break
        return dp[0]
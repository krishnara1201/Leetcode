class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        
        
        max_streak = 0

        for i in nums:
            if i - 1 not in seen:
                j = i
                current_streak = 0
                while j in seen:
                    current_streak += 1
                    j = j + 1
                max_streak = max(max_streak, current_streak)
        
        return max_streak
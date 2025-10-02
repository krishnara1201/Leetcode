class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        max_streak = 0

        for i in seen:
            if (i - 1) not in seen:
                length = 1
                while (i + length) in seen:
                    length += 1
                max_streak = max(max_streak, length)
        
        return max_streak

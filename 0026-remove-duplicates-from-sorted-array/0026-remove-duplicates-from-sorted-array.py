class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0
        i = 0
        while i + 1 < len(nums):
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                nums.pop(i+1)
            unique += 1
            i += 1

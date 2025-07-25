class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            if (target - nums[i]) in seen:
                return [i, seen[target - nums[i]]]
            
            if nums[i] not in seen:
                seen[nums[i]] = i
            
        
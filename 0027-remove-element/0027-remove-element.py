class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        l = len(nums)
        k = 0
        while i < l:
            if nums[i] == val:
                j = i
                while j < l-1:
                    nums[j] = nums[j+1]
                    j += 1
                l -= 1
            else:
                k += 1
                i+= 1
        return k
        
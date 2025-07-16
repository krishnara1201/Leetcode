class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums = sorted(nums)
        trip = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            twosum = self.two_sum(nums[i+1:], -nums[i])
            print(twosum)
            if len(twosum) > 0:
                for pair in twosum:
                    trip.append([nums[i], nums[i + pair[0] + 1], nums[i + pair[1] + 1]])
            
        return trip

    
    def two_sum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        res = []
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                res.append([l, r])
                l += 1
                while l < r and numbers[l] == numbers[l-1]:
                    l += 1
        return res


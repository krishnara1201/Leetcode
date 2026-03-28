class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        mode = 0
        for num in nums:
            if num == mode:
                count += 1
            elif count > 0:
                count -= 1
            else:
                mode = num
                count += 1
        
        return mode
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        swaps = 0

        while l <= r:
            if nums[l] == nums[r]:
                l += 1
                r -= 1
            while nums[l] != nums[r] and l <= r:
                if nums[l] < nums[r]:
                    nums[l+1] += nums[l]
                    l += 1
                else:
                    nums[r-1] += nums[r]
                    r -= 1

                swaps += 1
        return swaps

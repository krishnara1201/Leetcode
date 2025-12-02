class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_gas = 0
        for n in nums:
            if cur_gas < 0:
                return False
            elif n > cur_gas:
                cur_gas = n
            cur_gas -= 1
        return True

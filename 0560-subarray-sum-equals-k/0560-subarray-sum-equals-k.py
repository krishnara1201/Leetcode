class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum, res = 0, 0
        prefixSum = {0:1}
        for num in nums:
            cur_sum += num
            diff = cur_sum - k
            res += prefixSum.get(diff, 0)
            prefixSum[cur_sum] = prefixSum.get(cur_sum, 0) + 1
        
        return res
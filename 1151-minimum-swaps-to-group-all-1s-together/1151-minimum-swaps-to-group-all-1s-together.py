class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = 0
        n = len(data)
        for i in data:
            if i == 1:
                ones += 1
        
        if ones <= 1:
            return 0
        
        r = 0
        curr_swaps = 0
        while r < ones:
            if data[r] == 0:
                curr_swaps += 1
            r += 1
        
        l = 0
        res_swaps = curr_swaps
        while r < n:
            if data[r] == 0:
                curr_swaps += 1
            if data[l] == 0:
                curr_swaps -= 1
            r += 1
            l += 1
            res_swaps = min(curr_swaps, res_swaps)
        return res_swaps

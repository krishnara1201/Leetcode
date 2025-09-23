class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = max(candies)

        res = [False] * len(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= n:
                res[i] = True
        
        return res
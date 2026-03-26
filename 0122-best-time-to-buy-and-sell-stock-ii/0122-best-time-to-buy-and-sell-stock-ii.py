class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = total = 0
        for r in range(1,len(prices)):
            profit = prices[r] - prices[l]
            if profit > 0:
                total += profit
            l = r
        return total
            
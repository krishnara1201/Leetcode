class Solution:
    def rotatedDigits(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(1,n+1):
            if self.isrotatedvalid(i):
                dp[i] += 1
            dp[i] += dp[i-1]
        return dp[n]



    def isrotatedvalid(self, n:int) -> bool:
        s = str(n)
        if "3" in s or "4" in s or "7" in s:
            return False
        elif "2" in s or "5" in s or "6" in s or "9" in s:
            return True
        else:
            return False
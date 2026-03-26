class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = p2 = 0
        m, n = len(s), len(t)

        while p1 < m and p2 < n:
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        
        return True if p1 == m else False
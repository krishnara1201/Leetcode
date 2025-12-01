class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen = 0
        l = 0
        max_freq = 0
        visit = defaultdict(int)

        for r in range(len(s)):
            visit[s[r]] += 1
            max_freq = max(visit.values())
            if r - l + 1 - max_freq > k:
                visit[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)

        return maxlen
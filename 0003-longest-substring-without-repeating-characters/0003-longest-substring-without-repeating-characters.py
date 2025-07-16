class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        wind = set()
        max_wind = 0
        start = 0
        end = 0
        
        while end < n:
            if s[end] in wind:
                while s[start] != s[end] and start < end:
                    wind.remove(s[start])
                    start += 1
                wind.remove(s[start])
                start += 1    
                wind.add(s[end])
                end += 1
            else:
                wind.add(s[end])
                end += 1
            max_wind = max(max_wind, len(wind))
        
        return max_wind




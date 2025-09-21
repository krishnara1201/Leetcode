class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        ret_str = ""

        for i in range(min(n, m)):
            ret_str += word1[i] + word2[i]

        if n > m:
            ret_str += word1[m:]
        else:
            ret_str += word2[n:]
        
        return ret_str
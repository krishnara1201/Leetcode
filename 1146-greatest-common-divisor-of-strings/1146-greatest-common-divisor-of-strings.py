class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1 + str2 == str2 + str1:
            n, m = len(str1), len(str2)
            s = str1 + str2
            ret_str = ""

            for i in range(1, min(n, m) + 1):
                if (m + n) // i == (m + n) / i:
                    if s[:i] * int((n)/ (i)) == str1 and s[:i] * int((m)/ (i)) == str2:
                        ret_str = s[:i]
            
            return ret_str

        else:
            return ""
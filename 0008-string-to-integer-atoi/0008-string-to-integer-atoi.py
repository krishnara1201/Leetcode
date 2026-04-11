class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        numset = set("1234567890")
        i = 0
        pos = True
        num_list = []
        
        if n == 0:
            return 0
        
        while i < n and s[i] == " ":
            i += 1
        if i < n:
            if s[i] == "+":
                i += 1
            elif s[i] == "-":
                pos = False
                i += 1
            
            while i < n and s[i] == "0":
                i += 1
            
            while i < n and s[i] in numset:
                num_list.append(int(s[i]))
                i += 1
            
            result = 0
            for i,n in enumerate(reversed(num_list)):
                result += (10 ** i ) * n
            
            result = result if pos else -result

            if result > 2**31 - 1:
                return 2**31 - 1
            elif result < -2**31:
                return -2**31
            else:
                return result

        else:
            return 0
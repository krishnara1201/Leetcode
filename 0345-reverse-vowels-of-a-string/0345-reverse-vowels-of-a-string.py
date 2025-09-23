class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")

        stack = []
        for i in s:
            if i in vowels:
                stack.append(i)
        ret = ""
        for i in s:
            if i in vowels:
                ret += stack.pop()
            else:
                ret += i
        
        return ret
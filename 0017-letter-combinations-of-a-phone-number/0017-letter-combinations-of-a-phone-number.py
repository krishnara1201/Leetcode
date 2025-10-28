class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        if n == 0:
            return []
        
        def dfs(i, stack):
            if i == n:
                res.append("".join(stack))
                return
            for j in digitToChar[digits[i]]:
                stack.append(j)
                dfs(i + 1, stack)
                stack.pop()
        
        dfs(0, [])
        return res
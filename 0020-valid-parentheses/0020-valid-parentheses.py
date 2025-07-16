class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        closed_dic ={")" : "(", 
        "]" : "[",
        "}" : "{"}

        dic = "({["
        stack = []
        n = 0

        for i in s:
            if i in dic:
                stack.append(str(i))
                n += 1
            elif n > 0 and closed_dic[i] == stack[n-1]:
                stack.pop(n-1)
                n -= 1
            else:
                return False
        
        if stack == []:
            return True
        else:
            return False
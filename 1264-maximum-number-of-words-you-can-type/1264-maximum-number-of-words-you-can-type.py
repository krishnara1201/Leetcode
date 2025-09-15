class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        
        word = True
        bl = set(brokenLetters)
        result = 0
        i = 0
        count_space = 0

        while i < (len(text)):
            if text[i] == " ":
                count_space += 1

            if word:
                if text[i] in bl:
                    result += 1
                    word = False
                i += 1

            else:
                if text[i] == " ":
                    word = True
                i += 1

        return count_space + 1 - result

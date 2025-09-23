class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = []

        word = ""
        for i in s:
            if word and i == " ":
                word_list.append(word)
                word = ""
            elif i != " ":
                word += i
            else:
                continue
        
        if word:
            word_list.append(word)
            
        ret = []
        while word_list:
            ret.append(word_list.pop())
        return " ".join(ret)
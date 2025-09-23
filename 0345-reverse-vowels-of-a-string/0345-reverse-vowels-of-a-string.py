class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")

        l, r = 0, len(s) - 1

        word = list(s)

        while l < r:
            if word[l] in vowels and word[r] in vowels:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
            elif word[l] in vowels:
                r -= 1
            elif word[r] in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        
        return "".join(word)
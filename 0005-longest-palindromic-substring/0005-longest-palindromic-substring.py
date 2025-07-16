class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s
        l = len(arr)
        i = 0
        j = 0
        sub = []
        while i < l:
            # case 1
            sub_p1 = arr[i]
            left = i
            right = i
            while (left > 0 and right < l - 1):
                left = left - 1
                right = right + 1
                if arr[left] == arr[right]:
                    sub_p1 = arr[left] + sub_p1 + arr[right]
                else:
                    break
                
            sub.append(sub_p1)
            i += 1
        
        while j < l - 1:
            # case 2
            if arr[j] == arr[j+1]:
                sub_p2 = arr[j] + arr[j+1]
                left = j
                right = j + 1
                while (left > 0 and right < l - 1):
                    left = left - 1
                    right = right + 1
                    if arr[left] == arr[right]:
                        sub_p2 = arr[left] + sub_p2 + arr[right]
                    else:
                        break
                sub.append(sub_p2)
                j += 1   
            else:
                j += 1   

        maxi = -1
        
        for i in sub:
            if len(i) > maxi:
                res = i
                maxi = len(i)
        return res
        
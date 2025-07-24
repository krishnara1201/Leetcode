class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dic = {}

        for i in strs:
            sor = "".join(sorted(i))
            print(sor)
            if sor in dic:
                dic[sor].append(i)
            else:
                dic[sor] = [i]
        
        ret = []
        for j in dic:
            ret.append(dic[j])
        
        return ret
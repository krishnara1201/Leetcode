class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        l , r = 1, max(piles) + 1
        while l < r:
            m = l + ((r-l)//2)
            hour_count = 0
            for i in piles:
                hour_count += math.ceil(float(i) / float(m))        
        
            if hour_count <= h:
                r = m
            else:
                l = m + 1
        
        return l
        


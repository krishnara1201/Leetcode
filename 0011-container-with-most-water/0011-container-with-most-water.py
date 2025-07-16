class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l = 0
        r = n - 1
        curr_max = 0
        while l < r:
            if height[l] < height[r]:
                curr_max = max((r-l)*height[l], curr_max)
                l += 1
            else:
                curr_max = max((r-l)*height[r], curr_max)
                r -= 1

        return curr_max

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        n = len(height)
        l,r = 0, n - 1

        max_left, max_right = height[l], height[r]
        filled = 0
        while l < r:
            if max_left < max_right:
                l += 1
                max_left = max(height[l], max_left)
                filled += max_left - height[l]
                
            else:
                r -= 1
                max_right = max(height[r], max_right)
                filled += max_right - height[r]
                
        return filled

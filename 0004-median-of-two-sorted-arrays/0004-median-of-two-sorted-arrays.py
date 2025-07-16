class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = nums1 + nums2
        final = sorted(merge)
        leng = len(final)
        if leng % 2 == 1:
            return final[int((leng - 1)/2)]
        else:
            return (final[int(leng/2 - 1)] + final[int(leng/2)])/2

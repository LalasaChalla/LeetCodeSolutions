class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        sum1, sum2 = sum(nums1), sum(nums2)
        c1, c2 = nums1.count(0), nums2.count(0)
        if c1 == 0 and sum1 < sum2 + c2:
            return -1
        if c2 == 0 and sum2 < sum1 + c1:
            return -1
        return max(sum1 + c1, sum2 + c2)

class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ans=[0]*n
        i=0
        while i<n:
            ans[i]=nums[nums[i]]
            i=i+1
        return ans 
            
        

class Solution(object):
    def findNumbers(self, nums):
        c=0
        for i in nums:
            n=i
            s=len(str(abs(n)))
            if s%2==0:
                c+=1
        return c
        
        

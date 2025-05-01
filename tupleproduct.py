class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        dict = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): 
                p= nums[i] * nums[j]  
                dict[p] += 1
        for key, value in dict.items():
            if value > 1:
                count += (value * (value - 1)) // 2
        return count * 8

        
        

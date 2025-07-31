class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        result=0
        while(i<j):
            area=min(height[i],height[j])*(j-i)
            result=max(result,area)

            if(height[i]<height[j]):
                i=i+1
            else:
                j=j-1
        
        return result


            



        

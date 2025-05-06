class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (divisor<0 or dividend<0) and (divisor!=dividend):
            sign=-1
        else:
            sign=1
        
        dividend=abs(dividend)
        divisor=abs(divisor)
        quotient=0

        while dividend>=divisor:
            dividend=dividend-divisor
            quotient+=1

        quotient=quotient*sign

        if quotient < -2**31:
            return -2**31
        if quotient > 2**31 - 1:
            return 2**31 - 1
        
        return quotient
        

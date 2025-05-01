class Solution(object):
    def reverse(self, x):
        if x<0:
            sign=-1
        else:
            sign=1
        x=abs(x)
        l=[int(d) for d in str(x)]
        l.reverse()
        m=int(''.join(map(str,l)))*sign
        
        if m < -2**31 or m > 2**31 - 1:
            return 0
        return m 
        

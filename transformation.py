class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        MOD = 10**9 + 7
        count=0
        for i in range(t):
            new_s=""
            for ch in s:
                if ch=='z':
                    new_s+="ab"
                else:
                    new_s=new_s+chr(ord(ch) + 1)
            s=new_s
        l=len(new_s)% MOD
        return l
        

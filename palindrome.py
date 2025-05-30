class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s1=str(x)
        s2=s1[::-1]
        return s1 == s2

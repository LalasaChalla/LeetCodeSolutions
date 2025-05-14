class Solution(object):
    def lengthAfterTransformations(self, s, t, nums):
        """
        :type s: str
        :type t: int
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        count=0
        letters = {chr(97 + i): i for i in range(26)}
        for i in range(t):
            new_s=[]
            for ch in s:
                v1=letters[ch]
                v2=nums[v1]
                for k in range(1, v2+1):
                    base_index = ord(ch) - ord('a')  
                    new_index = base_index + k       
                    wrapped_index = new_index % 26   
                    ascii_value = wrapped_index + ord('a')  
                    next_char = chr(ascii_value)     
                    new_s.append(next_char) 
            s = ''.join(new_s)

        return len(s) % MOD

                        




        
        

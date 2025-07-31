class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        curr_sum = 0
        map = {0: 1}

        for num in nums:
            curr_sum += num
            if (curr_sum - k) in map:
                count += map[curr_sum - k]
            map[curr_sum] = map.get(curr_sum, 0) + 1

        return count
        

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sum = sum(nums)
        n = len(nums)
        range_sum = n*(n+1)/2
        return range_sum - nums_sum
        
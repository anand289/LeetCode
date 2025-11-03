class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        nums_set = set(nums)
        output = []
        for i in range(1,len(nums)+1):
            if i not in nums_set:
                output.append(i)
        return output





        
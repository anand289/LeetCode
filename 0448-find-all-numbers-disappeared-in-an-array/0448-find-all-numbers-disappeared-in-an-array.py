class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hash_table = {}
        out = []

        for num in nums:
            hash_table[num] = 1

        for i in range(1,len(nums)+1):
            if i not in hash_table:
                out.append(i)
        return out
        





        
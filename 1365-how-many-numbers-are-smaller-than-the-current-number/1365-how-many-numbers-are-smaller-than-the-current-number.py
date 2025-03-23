class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hmap = {}
        nums_sorted = sorted(nums)
        ret = []
        for i,v in enumerate(nums_sorted):
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
                hmap[v] = k
            else:
                k = i
                hmap[v] = k

        for i in range(0,len(nums)):
            ret.append(hmap[nums[i]])

        return ret
        
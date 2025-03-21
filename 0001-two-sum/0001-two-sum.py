class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}
        ret = []
        for i,v in enumerate(nums):
            diff = target - v
            if diff in hmap.keys():
                ret.append(hmap[diff])
                ret.append(i)
                break
            else:
                hmap[v] = i
        return ret

        
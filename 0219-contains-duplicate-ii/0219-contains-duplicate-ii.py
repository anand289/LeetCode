class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hmaps = {}
        for i,v in enumerate(nums):
            if v in hmaps.keys():
                if i-hmaps[v] <= k:
                    return True
                else:
                    hmaps[v] = i
            else:
                hmaps[v] = i
        return False
        
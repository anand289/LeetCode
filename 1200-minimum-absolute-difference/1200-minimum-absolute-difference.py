class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_diff = float('inf')
        ret = []
        for i in range(0,len(arr)-1):
            if arr[i+1] - arr[i] < min_diff:
                min_diff = arr[i+1] - arr[i]
                ret = []
            if arr[i+1] - arr[i] == min_diff:
                pair = [arr[i],arr[i+1]]
                ret.append(pair)
        return ret

        
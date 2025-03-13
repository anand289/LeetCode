class Solution(object):
    def twoSum(self, numbers, target):
        res = {}
        ret = []
        found = 0
        for i,v in enumerate(numbers):
            diff = target - v
            if diff in res.keys():
                ret.append(res[diff]+1)
                ret.append(i+1)
                return ret
            else:
                res[v] = i
        return -1

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums.sort()
        # ret = []
        # res = []
        # for i in range(0,len(nums)-1): 
        #     if nums[i] >= 0:
        #         break     
        #     arr = []
        #     if nums[i] != 0 and nums[i] == nums[i-1] and i > 0:
        #         continue
        #     for j in range(i+1,len(nums)):
        #         diff = -nums[i] - nums[j]
        #         if nums[j] in arr:
        #             res.append(nums[i])
        #             res.append(diff)
        #             res.append(nums[j])
        #             if res not in ret:
        #                 ret.append(res)
        #             res = []
        #         else:
        #             arr.append(diff)
        # return ret


        nums.sort()
        ret = []
        res = []
        for i in range(0,len(nums)-1):
            if i > 0 and (nums[i] == nums[i-1]):
                continue 
            target = -nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                cursum = nums[left] + nums[right]
                if cursum == target:
                    res.append(nums[i])
                    res.append(nums[left])
                    res.append(nums[right])
                    ret.append(res)
                    left += 1
                    while (left<right) and (nums[left] == nums[left-1]):
                        left +=1
                    res = []
                elif cursum < target:
                    left += 1
                elif cursum > target:
                    right -= 1
        return ret
        



        
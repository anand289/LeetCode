class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        peak = arr[0]
        peak_idx = -1
        maximum = 0
        for i in range(1,len(arr)-1):
            if arr[i-1] <arr[i] > arr[i+1]:
                peak = arr[i]
                peak_idx = i
                left_idx = peak_idx
                right_idx = peak_idx
                left_side = 0
                right_side = 0
                while (left_idx >= 1) and (arr[left_idx-1]<arr[left_idx]):
                    left_side += 1
                    left_idx -= 1
                while (right_idx <= len(arr)-2) and (arr[right_idx+1]<arr[right_idx]):
                    right_side += 1
                    right_idx += 1
                cur_max = left_side + right_side + 1
                if cur_max > maximum:
                    maximum = cur_max
        return maximum
            
        
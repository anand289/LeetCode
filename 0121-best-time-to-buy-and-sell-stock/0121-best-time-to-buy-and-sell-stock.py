class Solution(object):
    def maxProfit(self, prices):
        max = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[r] < prices[l]:
                l += 1
                r = l + 1
            else:
                if prices[r]-prices[l] > max:
                    max = prices[r]-prices[l]
                r = r + 1
        return max
            
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        if n > 1:
            dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

        # n = 5
        # 0 1 2 3 4 5
        # 0 1 2 3 5 8
        
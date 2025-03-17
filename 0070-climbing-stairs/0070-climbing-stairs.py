class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Iterative
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        if n > 1:
            dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

        # # Recursive : TLE
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # n = 5
        # idx:    0 1 2 3 4 5
        # output: 0 1 2 3 5 8
        
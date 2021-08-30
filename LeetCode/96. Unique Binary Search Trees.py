class Solution(object):
    def numTrees(self, n):
        if n == 1:
            return n

        dp = [0]*(n+1)
        dp[0],dp[1] = 1,1

        for i in range(2,n+1):

            for j in range(0,i):
                dp[i] += dp[j]*dp[i-j-1]

        return dp[-1]



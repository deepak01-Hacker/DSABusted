class Solution(object):
    def uniquePaths(self, row, col):
        
        dp = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(0,row):
            dp[i][0] = 1
        for i in range(0,col):
            dp[0][i] = 1

        for i in range(1,row):
            for j in range(1,col):
                dp[i][j] += dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

        

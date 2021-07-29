class Solution(object):
    def uniquePathsWithObstacles(self, dp):
        row = len(dp)
        col = len(dp[0])
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if dp[i][j] == 1:
                    dp[i][j] = -1


        for i in range(0,row):
            if dp[i][0] != -1:
                dp[i][0] = 1
            else:
                break
        for i in range(0,col):
            if dp[0][i] != -1:
                dp[0][i] = 1
            else:
                break

        for i in range(1,row):
            for j in range(1,col):
                
                if dp[i][j] != -1:
                    
                    if dp[i][j-1] != -1:
                        dp[i][j] += dp[i][j-1]
                        
                    if dp[i-1][j] != -1:
                        dp[i][j] += dp[i-1][j]
                        
        return dp[-1][-1] if dp[-1][-1] > 0 else 0

        

#User function Template for python3

class Solution:

    def ncr(self,n,r):
        if r == 0 or n == r:
            return 1
        return self.ncr(n-1,r-1)+self.ncr(n-1,r)
        
    def nCr(self, n, k):
        dp = [[ 0 for _ in range(k+1)] for _ in range(n+1)]
        
        for i in range(0,n+1):
            for j in range(0,(min(i,k)+1)):
                if j == 0 or i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
        return dp[n][k] % 1000000007
        

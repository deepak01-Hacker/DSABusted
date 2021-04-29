class Solution:
	def minimumCost(self, arr, n, W):
	    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
        for i in range(n+1):
            for j in range(W+1):
                if i == 0:
                    dp[i][j] = 10**9
                elif j == 0:
                    dp[i][j] = 0
                elif i <= j and arr[i-1] != -1 :
                    dp[i][j] = min(dp[i-1][j],arr[i-1]+dp[i][j-i])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][W] if dp[i][j] != 1000000000 else -1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,w = input().split()
		n,w = int(n),int(w)
		a = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minimumCost(a,n,w)
		print(ans)

# } Driver Code Ends

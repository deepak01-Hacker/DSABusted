#gFg Practice :- https://practice.geeksforgeeks.org/problems/longest-subsequence-such-that-difference-between-adjacents-is-one4724/1

class Solution:
    def longestSubsequence(self, n, arr):
        dp = [1]*n
        for i in range(n):
            for j in range(i+1,n):
                if abs(arr[i]-arr[j]) == 1 and dp[j] < dp[i]+1:
                    dp[j] = dp[i]+1
        return max(dp)
       

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = input().split()
        for itr in range(N):
            A[itr] = int(A[itr])
        
        ob = Solution()
        print(ob.longestSubsequence(N, A))
# } Driver Code Ends

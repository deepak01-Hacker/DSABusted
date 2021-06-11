class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]

        ans = 0

        for i in range(1,len(s)+1):
            dp[i][i] = 1

        #print(n)
        for diff in range(2,n+1):
            for i in range(n-diff+1):
                j = i+diff-1

                #print(s[i],s[j])          it helps to think broad
                if s[i] == s[j]:
                    print(True)
                    if diff == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1]+2

                ans = max(ans,dp[i][j])

        #print(dp)
        return ans

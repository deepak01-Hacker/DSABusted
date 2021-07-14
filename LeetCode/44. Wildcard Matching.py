class Solution(object):
    def isMatch(self, str, pat):
        n = len(str)
        m = len(pat)

        if m == 0:
            return n == 0

        dp = [[False for i in range(m+1)] for j in range(n+1)]

        dp[0][0] = True

        for j in range(1,m+1):
            if pat[j-1] == "*":
                dp[0][j] = dp[0][j-1]

        for i in range(1,n+1):
            for j in range(1,m+1):

                if pat[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

                elif pat[j-1] == "?" or str[i-1] == pat[j-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[n][m]

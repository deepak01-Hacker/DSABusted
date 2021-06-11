


#-----------------------------------------------

def lpSubstring(s):

    n = len(s)

    dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
    
    for i in range(1,len(s)+1):
        dp[i][i] = 1
    
    for diff in range(2,n+1):
        for i in range(n-diff+1):
            j = i+diff-1

            if s[i] == s[j]:
                if diff == 2:
                    dp[i][j] = 2
                    continue
                dp[i][j] = dp[i+1][j-1]+2
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j-1])

    return dp[0][n-1]





#------------------------- Work for some cases ------------------------

import sys

#bin/python3!


def longestPalindromeSubsequence(string,n):

    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if string[i-1] == string[-j]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[n][n]


if __name__ == "__main__":
    string = "GEEKSFORGEEKS"
    print(longestPalindromeSubsequence(string,len(string)))

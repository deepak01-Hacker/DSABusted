class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        if s == "":
            return ""
        
        n = len(s)

        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]

        ans = 1

        startIndex = 0

        for i in range(1,len(s)+1):
            dp[i][i] = 1

        for i in range(n-1):
            if s[i] == s[i+1]:
                ans = 2
                startIndex = i
                dp[i][i+1] = 2



        #print(n)
        for diff in range(2,n+1):
            for i in range(n-diff+1):
                j = i+diff-1


                if s[i] == s[j] and dp[i+1][j-1] != 0:
                    if diff == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1]+2
                        if ans < dp[i][j]:
                            ans = dp[i][j]
                            startIndex = i

        #print(dp)

        return s[startIndex:startIndex+ans]

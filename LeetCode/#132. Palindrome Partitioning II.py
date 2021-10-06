class Solution(object):
    
    def isValid(self,s):
        return s == s[::-1]


    def minCut(self, s):

        if s == "":
            return 0
        
        if self.isValid(s):
            return 0

        dp = [2001]*(len(s)+1)

        for i in range(len(s)):
            for j in range(i+1,len(s)+1):

                if self.isValid(s[i:j]):
                    left = 0
                    if i-1 >= 0:
                        left = dp[i]
                    dp[j] = min(left+1,dp[j])

        return dp[-1]-1

        

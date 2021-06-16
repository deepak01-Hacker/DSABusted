class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        len_s = len(s)
        len_p = len(p)
        
        if len_s == 0 and len_p == 0:
            
            return True
        if len_p == 0:
            return False
        
        dp = [[False for _ in range(len_p+1)] for _ in range(len_s+1)]
        
        dp[0][0] = True
        
        for i in range(2,len_p+1):
            if p[i-1] == "*":
                dp[0][i] = dp[0][i-2]
                
        for i in range(1,len_s+1):
            for j in range(1,len_p+1):
                
                if s[i-1] == p[j-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                    
                elif j > 1 and p[j-1] == "*":
                    dp[i][j] = dp[i][j-2]
                    if p[j-2] == "." or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                        
        return dp[len_s][len_p]

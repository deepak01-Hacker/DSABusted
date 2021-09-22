

"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.
A string's subsequence is a new string formed from the original string by deleting some (can be none) of 
the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).
It is guaranteed the answer fits on a 32-bit signed integer.


Input: s = "rabbbit", t = "rabbit"
Output: 3

Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit

Example 2:

"""
def subSequence(s,t):

    if t == "":
        return 1

    if s == "":
        return 0

    if s[-1] == t[-1]:
        return subSequence(s[:-1],t[:-1])+subSequence(s[:-1],t)

    return subSequence(s[:-1],t)

def optimizedSubsequence(s,t):

    dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]


    for i in range(len(s)+1):
        for j in range(len(t)+1):

            if j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = 0
            
            elif s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1] 

    

if __name__ ==  "__main__":

    s = "babgbag"
    t = "bag"

    print(optimizedSubsequence(s,t))

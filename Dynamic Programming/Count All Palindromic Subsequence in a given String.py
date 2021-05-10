
dp = [[-1 for _ in range(100)] for _ in range(100)]


def util(i,j):
    if i > j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]
    if (i == j):
        dp[i][j] = 1
        return dp[i][j]
    elif st[i] == st[j]:
        dp[i][j] = util(i+1,j) + util(i,j-1)+1
        return dp[i][j]
    else:
        dp[i][j] = util(i+1,j) + util(i,j-1) - util(i+1,j-1)
        return dp[i][j]
    

def recursionCountpalindrome(st):
    i = 0
    j = len(st)-1
    return util(i,j)

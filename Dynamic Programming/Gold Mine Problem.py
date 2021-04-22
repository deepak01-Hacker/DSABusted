#pyhon3

def isSafe(n,m,i,j):
    return i > 0 and j > 0 and i <= n and j <= m

def goldMine(arr):
    n = len(arr)
    m = len(arr[0])
    dp = [[0 for _ in range(len(arr[0])+1)] for _ in range(len(arr)+1)]
    for i in range(len(arr)):
        dp[i][1] = arr[i][0]
    maxs = -100000000
    for c in range(1,len(arr)+1):
        for r in range(1,len(arr)+1):
            left = dp[r][c-1]
            leftDown = 0
            leftUp = 0
            if isSafe(n,m,r+1,c-1):
                leftDown = dp[r+1][c-1]
            if isSafe(n,m,r-1,c-1):
                leftUp = dp[r-1][c-1]
            dp[r][c] = max(left+arr[r-1][c-1],leftDown+arr[r-1][c-1],leftUp+arr[r-1][c-1])
            maxs = max(maxs,dp[r][c])
    print(dp)
    return maxs

            
            

if __name__ == "__main__":
    arr = [[1, 3, 1, 5],
           [2, 2, 4, 1],
           [5, 0, 2, 3],
           [0, 6, 1, 2]]
    print(goldMine(arr))

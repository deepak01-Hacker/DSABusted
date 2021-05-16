
#from os import rename

#----------------------- Memoization --------------------------

dp = [[0 for _ in range(100)] for _ in range(100)]

def util(arr,i,j):
    if i > j:
        return 0
    if dp[i][j] != 0:
        return dp[i][j]
    dp[i][j] = max(arr[i]+util(arr,i+2,j),arr[j]+util(arr,i,j-2))
    return dp[i][j]

def optimalGame(arr):
    i = 0 
    j = len(arr)-1
    return util(arr,i,j)



if __name__ == "__main__":
    arr = [20, 30, 2, 2, 2, 10]
    print(dp(arr))

# ---------------------- Tabulation -------------------------
#GFG : https://practice.geeksforgeeks.org/problems/optimal-strategy-for-a-game-1587115620/1


#User function Template for python3


#Function to find the maximum possible amount of money we can win.
def optimalStrategyOfGame(arr, n):
    table = [[0 for i in range(n)]
                for i in range(n)]
 
    for gap in range(n):
        for j in range(gap, n):
            i = j - gap
            
            x = 0
            if((i + 2) <= j):
                x = table[i + 2][j]
            y = 0
            if((i + 1) <= (j - 1)):
                y = table[i + 1][j - 1]
            z = 0
            if(i <= (j - 2)):
                z = table[i][j - 2]
            table[i][j] = max(arr[i] + min(x, y),
                              arr[j] + min(y, z))
    return table[0][n - 1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        print(optimalStrategyOfGame(arr,n))#


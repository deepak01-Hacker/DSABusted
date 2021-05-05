import sys

#bin/python3!

def util(arr,n,sum):
    if sum == 0:
        return True
    if n < 0 or sum < 0:
        return False
    return util(arr,n-1,sum) or util(arr,n-1,sum-arr[n])


def dp_(arr,sum):
    dp = [[False for _ in range(sum+1)] for _ in range(len(arr)+1)]

    for i in range(len(arr)+1):
        for j in range(sum+1):
            if j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            elif arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(arr)][sum]

if __name__  == "__main__":
    arr = [1,5,11,5]
    print(dp_(arr,13))


#from os import rename


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
    arr = [15,8,3,7]
    print(optimalGame(arr))

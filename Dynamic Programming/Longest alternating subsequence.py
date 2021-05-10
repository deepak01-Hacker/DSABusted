#!bin/python3 


# ----------------------------------- Recursion Approach by a Noob

def util(arr,n,n_1,mod):
    if n <= -1 or n_1 <= -1:
        return 0
    if mod == "ga" and arr[n] > arr[n_1]:
        return max(util(arr,n_1,n_1-1,"la")+1,util(arr,n,n_1-1,"ga"))
    elif mod == "la" and arr[n] < arr[n_1]:
        return max(util(arr,n_1,n_1-1,"ga")+1,util(arr,n,n_1-1,"la"))
    return max(util(arr,n,n_1-1,mod),util(arr,n_1,n_1-1,mod))


def longestAlternateSubsequence(arr):
    if arr == []:
        return 0
    n = len(arr)-1
    return max(util(arr,n,n-1,"la"),util(arr,n,n-1,"ga"))+1


#--------------------------------- LCS trick -------------------------


def longestAlternateSubsequence(arr):
    if arr == []:
        return 0
    n = len(arr)
    dp = [[-1,1] for _ in range(n)]

    maxs = 1
    for i in range(0,n):
        for j in range(i+1,n):

            if dp[i][0] == -1:
                dp[j][0] = arr[i]
                dp[j][1] = dp[i][1] + 1
        
            elif (((arr[i] < arr[j] and dp[i][0] > arr[i]) 
                        or (arr[i] > arr[j] and dp[i][0] < arr[i]))
                                and dp[j][1] < dp[i][1] + 1):
                dp[j][0] = arr[i]
                dp[j][1] = dp[i][1] + 1

            maxs = max(dp[j][1],maxs)
    return maxs
            

if __name__ == "__main__":
    #arr = [1,5,4]
    arr = [1,17,5,10,13,15,10,5,16,8]
    print(longestAlternateSubsequence(arr))

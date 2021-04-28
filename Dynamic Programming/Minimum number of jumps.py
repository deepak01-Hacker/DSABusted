

def optimized(arr):
    n = len(arr)
    jumps , currend ,currfar = 0,0,0
    for i in range(len(arr)):
        currfar = max(currfar,i+arr[i])
        if (i == currend):
            jumps += 1
            currend = currfar
        if currend >= n-1:
            return jumps
    return -1 if currend < n-1 else jumps

def util(arr,n,next):
    if n == 0:
        print(arr,n,next)
        return 1

    if arr[n] == 0 or next == 0:
        return 10**6
    return min(util(arr,n-1,next-1),util(arr,n-1,next+arr[n]-1)+1)


def dpUtil(arr):
    dp = [float('inf') for _ in range(len(arr))]
    dp[0] = 0

    for i in range(len(arr)):
        for j in range(i+1,min(len(arr),arr[i]+i+1)):
            if arr[j] == 0:
                break
            if dp[j] > dp[i]+1:
                dp[j] = dp[i]+1
    return dp[-1] 
    


def minimumNumber(arr):
    if (len(arr)>0 and arr[-1] == 0) or (len(arr) == 0):
        return 0
    return dpUtil(arr)
    next = arr[-1]
    #return util(arr,len(arr)-1,next)+1

#print(minimumNumber([1,4,3,2,6,7]))

print(optimized([1 ,3 ,5 ,8 ,9 ,2 ,6 ,7 ,6 ,8 ,9]))

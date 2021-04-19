
dp = {}

def util(arr,start,high):
    if high == start:
        return 0
    try:
        if dp[(start,high)]:
            return dp[(start,high)]
    except:
        min_ = 10**7
        for k in range(start,high):
            dp[(start,high)] = util(arr,start,k)+util(arr,k+1,high) + arr[start-1]*arr[k]*arr[high]
            min_ = min(min_,dp[(start,high)])
        return min_

def matrixchainMultiplication(arr):
    return util(arr,1,len(arr)-1)


if __name__ == "__main__":
    arr = [40, 20, 30, 10, 30]
    print(matrixchainMultiplication(arr))

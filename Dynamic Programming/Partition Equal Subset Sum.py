def isPossibleTOpartitionInEqualsum(arr):
    sumA = sum(arr)
    if sumA%2 == 1:
        return False
    sumA = sumA//2
    return dp(arr,len(arr),sumA)

def dp(arr,n,sumA):
    
    table = [[False for _ in range(sumA+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(sumA+1):
            if j == 0:
                table[i][j] = True
            elif i == 0:
                table[i][j] = False
            elif arr[i-1] <= j:
                table[i][j] = table[i-1][j-arr[i-1]] or table[i-1][j]
            else:
                table[i][j] = table[i-1][j]
    return table[n][sumA]


if __name__ == "__main__":
    arr = [478, 757 ,314 ,471 ,729 ,100 ,459 ,618]
    print(sum(arr)/2)
    print(isPossibleTOpartitionInEqualsum(arr))

# Problem : Maximum profit by buying and selling a share at most twice



# ----------------------------------- REcursion- ---------------------------------------------

def util(arr,buy,sell,k):
    #here k is check user only can buy at most twice share 
    if sell < 1 or buy < 0:
        return 0
    if k == 2:
        return 0
    return max((arr[sell]-arr[buy])+util(arr,buy-2,buy-1,k+1),util(arr,buy-1,sell,k),util(arr,buy-2,buy-1,k))


def stockTwo(arr):
    sell = len(arr)-1 #sell and buy are pointers 
    buy = sell-1
    return util(arr,buy,sell,0)

#---------------------------------- DP Tabulation ------------------------------------------------


def DP(arr):
    
    dp = [[0,0] for _ in range(len(arr))]

    result = 0

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if i >= 2 :
                dp[j][1] = max(dp[i-1][0],dp[j][1])
            if arr[i] < arr[j] and dp[j][0] < arr[j]-arr[i]:
                dp[j][0] = arr[j] - arr[i]
            
            result = max(result,dp[j][1]+arr[j]-arr[i],dp[j][0])
    return result




if __name__ == "__main__":
    arr = [10, 22, 5, 75, 65, 80]            # ans 87
    #arr = [2, 30, 15, 10, 8, 25, 80]        # ans 100
    #arr = [90, 80, 70, 60, 50]              # ans 0
    print(DP(arr))

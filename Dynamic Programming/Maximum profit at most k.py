def maxProfit(prices, n, k):
     
    # Bottom- DP approach
    profit = [[0 for i in range(k + 1)]
                 for j in range(n)]
     
    for i in range(1, n):
         
        for j in range(1, k + 1):
            max_so_far = 0
             
            for l in range(i):
                max_so_far = max(max_so_far, prices[i] -
                            prices[l] + profit[l][j - 1])
                             
            profit[i][j] = max(profit[i - 1][j], max_so_far)
     
    return profit[n - 1][k]
 
k = 2
prices = [10, 22, 5, 75, 65, 80]
n = len(prices)
 
print("Maximum profit is:",
       maxProfit(prices, n, k))

#---------------------- o(n2)------------------

def maxProfit(price, n, k):

    profit = [[0 for i in range(n + 1)]
                 for j in range(k + 1)]
 
    # Fill the table in bottom-up fashion
    for i in range(1, k + 1):
        prevDiff = float('-inf')
         
        for j in range(1, n):
            prevDiff = max(prevDiff,
                           profit[i - 1][j - 1] -
                           price[j - 1])
            profit[i][j] = max(profit[i][j - 1],
                               price[j] + prevDiff)
 
    return profit[k][n - 1]
 
if __name__ == "__main__":
 
    k = 3
    price = [12, 14, 17, 10, 14, 13, 12, 15]
    n = len(price)
 
    print("Maximum profit is:",
           maxProfit(price, n, k))

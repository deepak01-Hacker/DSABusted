
"""
#Medium

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.


"""


def stockMaxProfit(prices):

    min = prices[0]

    dp = [0]*len(prices)

    for i in range(0,len(prices)):
        for j in range(i+1,len(prices)):

            
            if prices[j] > prices[i]:
                profit = prices[j]-prices[i]
                profit += dp[i-1] if i-1 >= 0 else 0

                dp[j] = max(dp[j],profit)
            else:
                dp[j] = max(dp[j],dp[j-1])
            
    return max(dp)

def stockMarket(prices):
    #peak Vally Solution 

    maxProfit = 0

    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            maxProfit += prices[i]-prices[i-1]
    
    return maxProfit





if __name__ == "__main__":
    prices = [7,1,5,3,6,4]

    print(stockMaxProfit(prices))

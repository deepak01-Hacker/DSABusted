class Solution(object):
    def maxProfit(self, prices):
        profit = 0

        left = [0]*len(prices)
        right = [0]*len(prices)

        leftMin = prices[0]

        for i in range(1,len(prices)):

            leftMin = min(leftMin,prices[i])

            left[i] = max(left[i-1],prices[i]-leftMin)

        rightMax = prices[-1]


        for i in range(len(prices)-2,-1,-1):

            rightMax = max(rightMax,prices[i])

            right[i] = max(right[i+1],rightMax-prices[i])

            profit = max(profit,left[i]+right[i+1])

        #print(profit) 
        return max(profit,max(left),max(right))
    

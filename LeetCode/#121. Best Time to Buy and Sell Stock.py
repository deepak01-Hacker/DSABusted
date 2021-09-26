class Solution(object):
    def maxProfit(self, prices):
    
    
        ans = 0
       
        buy = (10**5)+1
       
        for i in range(len(prices)):
            ans = max(ans,prices[i]-buy)
           
            buy = min(buy,prices[i])
       
        return ans


        

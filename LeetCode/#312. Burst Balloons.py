
class Solution(object):

    def maxCoins(self, nums):
        
        if (len(nums) == 0):
            return 0;
        nums.insert(0, 1);
        nums.append(1);
        n = len(nums)
        l = 0
        r = 0

        dp = [[0 for _ in range(n)] for _ in range(n)]

        for k in range(2,n): # length
            for l in range(0,n-k): 
                r = l+k;
                for i in range(l+1,r) :
                    dp[l][r] = max(dp[l][r], nums[l]*nums[i]*nums[r]+dp[l][i]+dp[i][r]);



        return dp[0][n-1];





dp = {}
class Solution(object):
    def boundHandle(self,i,nums):
        if i < 0 or i >= len(nums):
            return 1
        return nums[i]

    def burstBallon(self,nums):
        
        if tuple(nums) in dp:
            return dp[tuple(nums)]

        ans = 0
        for i in range(len(nums)):
            coins = (self.boundHandle(i-1,nums)*nums[i]*self.boundHandle(i+1,nums)) + self.burstBallon(nums[:i]+nums[i+1:])
            ans = max(ans,coins)
        dp[tuple(nums)] = ans
        return ans


    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.burstBallon(nums)
        

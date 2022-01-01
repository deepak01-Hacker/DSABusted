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
        

class Solution(object):
    def rob(self, nums):
        if nums == []:
            return 0
        
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0],nums[1])
        
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        return max(dp)
        

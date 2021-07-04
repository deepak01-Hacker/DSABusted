class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        subArraySum = 0
        
        result = -10**6
        
        for i in range(len(nums)):
            
            subArraySum += nums[i]
            
            if subArraySum < nums[i]:
                subArraySum = nums[i]
                
            result = max(subArraySum,result)
            
        return result
        

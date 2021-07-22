class Solution(object):
    def canJump(self, nums):
        
        maxIndex = 0
        
        for i in range(len(nums)-1):
            
            maxIndex = max(i+nums[i],maxIndex)
            
            
            if maxIndex == i:
                return False
        
        return True if maxIndex >= len(nums)-1 else False

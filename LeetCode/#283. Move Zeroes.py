class Solution(object):
    def moveZeroes(self, nums):
        left = 0
        
        for i in range(len(nums)):
            
            if nums[i] != 0:
                
                nums[left] = nums[i]
                left += 1
        
        for i in range(left,len(nums)):
            nums[i] = 0
        
        

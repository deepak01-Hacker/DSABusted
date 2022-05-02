class Solution(object):
    def sortArrayByParity(self, nums):
        nums.sort(key=lambda x:x%2)
        return nums
    
        

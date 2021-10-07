class Solution(object):
    def reverse(self,left,right,nums):
        
        while(left<right):
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
    
    def rotate(self, nums, k):
        k = k%len(nums)
        
        self.reverse(0,(len(nums)-k)-1,nums)
        self.reverse((len(nums)-k),len(nums)-1,nums)
        self.reverse(0,len(nums)-1,nums)
       
        

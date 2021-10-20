class Solution(object):
    def sortColors(self, nums):
        low = 0
        mid = 0
        
        high = len(nums)-1
        
        while(mid<=high):
            switch = nums[mid]
            
            if switch == 0:
                nums[low],nums[mid] = nums[mid],nums[low]
                low += 1
                mid += 1
                
            elif switch == 2:
                nums[mid],nums[high] = nums[high],nums[mid]
                high -= 1
                
            else:
                mid += 1
                







#=================================================================================================================

class Solution(object):
    def sortColors(self, nums):
        counterOne = 0
        counterZero = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                counterOne += 1
            elif nums[i] == 0:
                counterZero += 1
                
        counterTwo = len(nums)-(counterOne+counterZero)
        
        for i in range(len(nums)):
            if counterZero :
                nums[i] = 0
                counterZero -= 1
            elif counterOne :
                nums[i] = 1
                counterOne -= 1
            else:
                nums[i] = 2
                counterTwo -= 1
        return nums

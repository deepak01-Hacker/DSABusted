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

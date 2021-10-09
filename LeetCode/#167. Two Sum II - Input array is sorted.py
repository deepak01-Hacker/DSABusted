class Solution(object):
    def twoSum(self, numbers, target):
        
        left = 0
        right = len(numbers)-1
        
        while(left<right):
            
            pairSum = numbers[left]+numbers[right]
            
            if pairSum == target:
                return [left+1,right+1]
            
            elif pairSum > target:
                right -= 1
            else:
                left += 1

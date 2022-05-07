class Solution(object):
    def find132pattern(self, nums):
        ak = -10**26
        stack = []

        for i in range(len(nums)-1,-1,-1):
            if nums[i] < ak:
                return True
            while(stack and stack[-1] < nums[i]):
                ak = stack.pop()
            stack.append(nums[i])
        return False
            
        
        

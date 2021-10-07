class Solution(object):
    def findSeprate(self,nums):
        left = 0
        right = len(nums) - 1
        
        while(left<=right):
            mid = (left+right)//2
            
            if (nums[mid] >= 0 and ((mid-1 >= 0 and nums[mid-1] < 0) or (mid-1 < 0))):
                return mid
            elif nums[mid] >= 0 :
                right = mid-1
            else:
                left = mid+1
        
        return -1
        
    
    
    def sortedSquares(self, nums):
        
        if nums == []:
            return []
        
        result = []
        
        point = self.findSeprate(nums)
        
        left = -1
        right = len(nums)
        
        point = self.findSeprate(nums)
        
        if point > -1:
            
            right = point
            left = point-1
            
        elif nums[0] < 0 and nums[-1] < 0:
            left = len(nums)-1
        else:
            right = 0
        
        while(left >= 0 and right <= len(nums)-1):
            
            if abs(nums[left]) < nums[right]:
                result.append((nums[left])**2)
                
                left -= 1
                
            else:
                result.append((nums[right]**2))

                right += 1
                
        while(left >= 0):
            result.append((nums[left])**2)
            
            left -= 1
        
        while(right <= len(nums)-1):
            result.append((nums[right])**2)
            right += 1
            
        return result 


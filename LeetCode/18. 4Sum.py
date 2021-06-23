
#------------------o(n3) Solution ------------- but acceptable------------------------

class Solution(object):
    def fourSum(self, nums, tr):
        res = set()
        
        nums.sort()
        
        n = len(nums)
        
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left = j+1
                right = n-1
                
                while(left<right):
                    
                    currentSum = nums[i]+nums[j]+nums[left]+nums[right]
                    
                    if currentSum == tr:
                    
                        res.add((nums[i],nums[j],nums[left],nums[right]))
                        left += 1
                        
                    elif currentSum < tr:
                        left += 1
                    else:
                        right -= 1
        return list(res)
 
 #------------------------ O(n2) ---------------------------------------------
 
 
def quadruplets(nums,tr):
    res = set()

    checker = {}
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            checker[nums[i]+nums[j]] = [i,j]
    
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):

            cSum = nums[i]+nums[j]

            if tr-cSum in checker :
                point = checker[tr-cSum]
                
                if point[0] > j :
                    #print(point,i,j)
                    res.add((nums[i],nums[j],nums[point[0]],nums[point[1]]))
    return list(res)

                        

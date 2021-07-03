class Solution(object):
    def searchInsert(self, nums, target):
        
        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)

        left = 0
        right = len(nums)-1

        while(left<=right):
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1

        return mid+1 if nums[mid] < target else mid

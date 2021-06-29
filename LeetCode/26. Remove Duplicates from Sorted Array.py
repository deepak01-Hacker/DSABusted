class Solution(object):
    def removeDuplicates(self, arr):
        
        left = 0

        for right in range(1,len(arr)):
            if arr[left] < arr[right]:
                arr[left+1] = arr[right]
                left += 1

        return left+1

        

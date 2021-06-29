class Solution(object):
    def removeElement(self, arr, val):
        if arr == []:
            return 0
        
        left = 0
        right = len(arr)-1

        while(left<right):
            if arr[right] == val:
                right -= 1
            elif arr[left] == val:
                arr[left],arr[right] = arr[right],arr[left]
                left += 1
                right -= 1
            else:
                left += 1
        return left+1 if arr[left] != val else left




        

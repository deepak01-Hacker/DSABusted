class Solution(object):
    def utilStart(self,left,right,arr,tr):
        if left > right:
            return -1
        mid = (left+right)//2

        if (arr[mid] == tr):
            if (mid-1 >= 0 and arr[mid] > arr[mid-1]) or mid == 0:
                return mid
            right = mid-1
        elif arr[mid] > tr:
            right = mid-1
        else:
            left = mid+1
        return self.utilStart(left,right,arr,tr)

    def utilEnd(self,left,right,arr,tr):
        if left > right:
            return -1

        mid = (left+right)//2

        if arr[mid] == tr:
            if (mid+1 < len(arr) and arr[mid+1] > arr[mid]) or mid == len(arr)-1:
                return mid
            left = mid+1


        elif arr[mid] > tr:

            right = mid-1
        else:
            left = mid+1
        return self.utilEnd(left,right,arr,tr)
    
    def searchRange(self, arr, tr):
        left = 0
        right = len(arr)-1
        
        res = [-1,-1]

        res[0] = self.utilStart(left,right,arr,tr)
        res[1] = self.utilEnd(left,right,arr,tr)
        return res

        

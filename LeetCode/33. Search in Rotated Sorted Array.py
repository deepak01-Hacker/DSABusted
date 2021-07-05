class Solution(object):
    def finder(self,left,right,arr,tr):
        if right < left:
            return -1
        
        mid = (left+right)//2
        
        #print(left,right,mid)

        if arr[mid] == tr:
            return mid
        
        if tr > arr[mid]:
            if arr[left] > arr[mid] and arr[right] < tr :
                right = mid-1
            else:
                left = mid+1
        elif tr < arr[mid]:
            if arr[mid] > arr[right] and tr <= arr[right]  :
                #print("yes")
                left = mid+1
            else:
                right = mid-1
        #print(left,right)
        return self.finder(left,right,arr,tr)
            
    def search(self, arr, target):
        return self.finder(0,len(arr)-1,arr,target)

        

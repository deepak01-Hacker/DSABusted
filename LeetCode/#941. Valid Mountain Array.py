class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        incre = False
        decre = False
        
        for i in range(1,len(arr)):
            if arr[i-1] < arr[i]:
                if decre:
                    return False
                incre = True
            elif arr[i-1] > arr[i]:
                decre = True
            elif arr[i-1] == arr[i]:
                return False
        return True if incre == True and decre == True else False
        

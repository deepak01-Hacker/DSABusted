class Solution(object):
    def firstMissingPositive(self, arr):
        if arr == []:
            return 1
        if len(arr) == 1 and arr[0] <= 0:
            return 1

        set = len(arr)

        for i in range(len(arr)):
            if arr[i] <= 0:
                arr[i] = set+1

        #print(arr,set)
        minusSet = -set

        for i in range(len(arr)):
            if arr[i]>=minusSet and arr[i] <= set:
                address = arr[i] if arr[i] > 0 else arr[i]*-1

                if arr[address-1] < 0:
                    continue
                arr[address-1] = -arr[address-1]
        #print(arr)


        for i in range(len(arr)):
            if arr[i] > 0:
                return i+1
        return set+1

                
        
        

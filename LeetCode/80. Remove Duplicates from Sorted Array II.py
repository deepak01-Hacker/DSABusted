class Solution(object):
    def removeDuplicates(self, arr):
        i = 0
        count = 1
        j = 0

        for j in range(1,len(arr)):
            #print(i,j)

            if arr[i] == arr[j]:
                count += 1
            else:
                count = 1

            arr[i+1] = arr[j]

            if count <= 2:
                i += 1
                
        return len(arr)-(j-i)

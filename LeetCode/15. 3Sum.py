class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        result = set()
        n = len(arr)
        arr.sort()

        #print(arr)
        for i in range(n-2):
            l = i+1
            r = n-1
            while(l<r):
                tripletSum = arr[i]+arr[l]+arr[r]
                if tripletSum == 0:
                    result.add((arr[i],arr[l],arr[r]))
                    l+=1
                elif tripletSum < 0:
                    l += 1
                else:
                    r -= 1
                    
        return list(result)
        
        

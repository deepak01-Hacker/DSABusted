class Solution:
    def threeSumClosest(self, arr: List[int], target: int) -> int:
        ans = 10**6
        
        n = len(arr)
        arr.sort()

        #print(arr)
        for i in range(n-2):
            
            l = i+1
            r = n-1
            
            while(l<r):
                tripletSum = arr[i]+arr[l]+arr[r]
                
                if abs(ans-target) > abs(tripletSum-target):
                    ans = tripletSum

                if tripletSum < target:
                    l += 1
                else:
                    r -= 1
                    
        return ans

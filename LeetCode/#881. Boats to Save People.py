class Solution(object):
    def numRescueBoats(self, arr, limit):
        
        arr.sort()

        i = 0
        j = len(arr)-1
        ans = 0

        while(i<j):
            if arr[j]+arr[i] > limit:
                j -= 1
            else:
                i += 1
                j -= 1
            ans += 1
            
        if i == j:
            ans += 1
            
        return ans


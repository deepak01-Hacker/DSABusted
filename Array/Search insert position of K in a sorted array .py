#User function Template for python3

class Solution:
    def searchInsertK(self, arr, N, k):
        res = 0
        
        if arr and arr[-1] < k:
            return N
        if arr and arr[0] > k:
            return 0
        
        left = 0
        right = N-1
        
        while(left<=right):
            mid = (left+right)//2
            
            if arr[mid] == k:
                return mid
            
            if arr[mid] < k:
                res = max(res,mid)
                left = mid+1
            else:
                right = mid-1
        return res+1
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends

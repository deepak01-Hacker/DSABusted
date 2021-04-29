#User function Template for python3

class Solution:
    def maximumPath(self, N, mat):
        mins = 0
        n = len(mat)
        for i in range(1,len(mat)):
            mat[i][0] += max(mat[i-1][0],mat[i-1][1])
            for j in range(1,len(mat)-1):
                mat[i][j] += max(mat[i-1][j],mat[i-1][j+1],mat[i-1][j-1])
                
            mat[i][n-1] += max(mat[i-1][n-2],mat[i-1][n-1])
                
        return max(mat[n-1])
                    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends

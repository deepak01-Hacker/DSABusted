
def downwardDigonal(n, A): 
    ans = []

    for j in range(n):
        i_ = 0
        j_ = j

        while(i_ < n and j_ >= 0):
            ans.append(A[i_][j_])

            i_ += 1
            j_ -= 1
    
    for i in range(1,n):
        i_ = i
        j_ = n-1

        while(i_ < n and j_ >= 0):
            ans.append(A[i_][j_])

            i_ += 1
            j_ -= 1

    return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDigonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends

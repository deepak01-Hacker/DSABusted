class Solution:
    def print_next_greater_freq(self,arr,n):
        ans = [-1]*n
        
        map = {}
        
        for i in range(0,n):
            try:
                map[arr[i]] += 1
            except:
                map[arr[i]] = 1
                
        stack = []
        for i in range(0,n):
            while(stack and arr[stack[-1]] != arr[i] and map[arr[stack[-1]]] < map[arr[i]]):
                index = stack.pop()
                ans[index] = arr[i]
            stack.append(i)
        return ans


#{ 
#  Driver Code Starts
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        obj=Solution()
        ans=obj.print_next_greater_freq(arr,n)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends

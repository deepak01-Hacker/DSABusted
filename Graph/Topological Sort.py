class Solution:
    # Your task is to complete this function
    # Function should return Topologically Sorted List
    # Graph(adj) is a list of List
    # V is no of Vertices
    def detectCycleUtil(self,graph,visited,u):
        if visited[u] == 1:
            return True
        if visited[u] == 2:
            return False
        
        visited[u] = 1
        for v in graph[u]:
            if self.detectCycleUtil(graph,visited,v):
                return True
        visited[u] = 2
        return False
    
    
    def detectCycle(self,graph,n):
        visited = [0 for _ in range(n)]
        for u in range(n):
            if visited[u] == 0:
                if self.detectCycleUtil(graph,visited,u):
                    return True
        return False
    
    def dfs(self,graph,u,visited,stack):
        visited[u] = True
        for v in graph[u]:
            if visited[v] == False:
                self.dfs(graph,v,visited,stack)
        stack.append(u)
    
    
    def topologicalSort(self,graph,n):
        ans = []
        if self.detectCycle(graph,n):
            return ans
        stack = []
        visited = [False for _ in range(n)]
        for u in range(n):
            if visited[u] == False :
                self.dfs(graph,u,visited,stack)
        return stack[::-1]

    def topoSort(self, V, adj):
        return self.topologicalSort(adj,V)
        


#{ 
#  Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends

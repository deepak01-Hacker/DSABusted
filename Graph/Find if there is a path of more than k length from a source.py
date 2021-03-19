
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ Find if there is a path of more than k length from a source

class Solution:
    
    def __init__(self,V):
        self.V = V
        self.adj = [[] for _ in range(self.V)]
    
    def addEdge(self,u,v,w):
        self.adj[u].append([v,w])
        self.adj[v].append([u,w])
    
    def dfs(self,u,visited,k):
        if k<=0:
            return True
        for v,w in self.adj[u]:
            if visited[v] == False:
                visited[v] = True
                if self.dfs(v,visited,k-w):
                    return True
                visited[v] = False
        return False


    def findPath(self,src,k):
        visited = [False]*self.V
        visited[src] = True
        return self.dfs(src,visited,k)

if __name__ == "__main__":
    g = Solution(9)
    g.addEdge(0, 1, 4)  
    g.addEdge(0, 7, 8)  
    g.addEdge(1, 2, 8)  
    g.addEdge(1, 7, 11)  
    g.addEdge(2, 3, 7)  
    g.addEdge(2, 8, 2)  
    g.addEdge(2, 5, 4)  
    g.addEdge(3, 4, 9)  
    g.addEdge(3, 5, 14)  
    g.addEdge(4, 5, 10)  
    g.addEdge(5, 6, 2)  
    g.addEdge(6, 7, 1)  
    g.addEdge(6, 8, 6)  
    g.addEdge(7, 8, 7)
    src = 0
    k  = 62
    print(g.findPath(src,k))

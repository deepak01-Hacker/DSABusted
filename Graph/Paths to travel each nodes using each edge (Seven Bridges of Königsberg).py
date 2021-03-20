
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ Eular Graph and Paths to travel each nodes using each edge (Seven Bridges of Königsberg)
#variation of Eular Graph

class Graph:

    def __init__(self,V):
        self.V = V
        self.adj = [[] for _ in range(self.V)]

    def addEdge(self,u,v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self,u,visited):
        visited[u] = True
        count = 0
        for v in self.adj[u]:
            if visited[v] == False:
                count += self.dfs(v,visited)
        return count
    
    def rmvEdge(self,u,v):
        uv = self.adj[u].index(v)
        vu = self.adj[v].index(u)
        self.adj[u][uv] = -1
        self.adj[v][vu] = -1
    
    def isValidNextEdge(self,u,v):
        count = 0
        for i in self.adj[u]:
            if i != -1:
                count += 1
        if count == 1:
            return True
        visited = [False]*self.V
        count1 = self.dfs(u,visited)

        self.rmvEdge(u,v)
        visited = [False]*self.V
        count2 = self.dfs(v,visited)

        self.addEdge(u,v)

        if count1 > count2:
            return False
        return True


    def printEularPath(self,u):
        for i in self.adj[u]:
            v = i
            if v != -1 and self.isValidNextEdge(u,v):
                print(str(u) + " - "+str(v),end=" ")
                self.rmvEdge(u,v)
                self.printEularPath(v)


    def findEular(self):
        u = 0
        for i in range(self.V):
            if (len(self.adj[u]) & 1):
                u = i
                break
        self.printEularPath(u)
        print()


if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(0,3)
    g.addEdge(0,2)
    g.addEdge(0,4)
    g.addEdge(1,2)
    g.addEdge(3,4)
    print(g.findEular())


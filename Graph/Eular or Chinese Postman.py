
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ Eular Graph and Chinese Psotman Graph Problem 
# if Graph is Eular then the answer is sum of all vertex one time :)
# I think you got it main logic ! if don't then visit Tech dose Youtube channel for more explantion


class Graph:

    def __init__(self,V):
        self.V = V
        self.adj = [[] for _ in range(self.V)]

    def addEdge(self,u,v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self,u,visited):
        visited[u] = True
        for v in self.adj[u]:
            if visited[v] == False:
                self.dfs(v,visited)

    def isConnected(self):
        visited = [False]*self.V
        startU = -1
        for u in range(self.V):
            if len(self.adj[u]) > 0:
                startU = u
                break
        self.dfs(startU,visited)
        for u in range(self.V):
            if visited[u] == False and len(self.adj[u]) > 0:
                return False
        return True

    def findEular(self):
        if self.isConnected() == False:
            return 0
        odd = 0
        for u in range(self.V):
            if (len(self.adj[u]) & 1):
                odd += 1
        if odd > 2:
            return 0
        return 2 if odd == 0 else 1


    def findEularPathCycle(self):
        res = self.findEular()
        if res == 0:
            return "NOt Eular"
        elif res == 1:
            return "Semi Eular"
        else:
            return "Eular Graph"


if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(0,3)
    g.addEdge(0,2)
    g.addEdge(0,4)
    g.addEdge(1,2)
    g.addEdge(3,4)
    print(g.findEularPathCycle())


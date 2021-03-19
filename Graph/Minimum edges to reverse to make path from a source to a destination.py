
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ Minimum edges to reverse to make path from a source to a destination

class Graph:

    def __init__ (self,V):
        self.V = V
        self.adj = [[] for _ in range(self.V)]

    def addEdge(self,u,v):
        self.adj[u].append([v,0])
        self.adj[v].append([u,1])
    
    def selectMinimum(self,dist,visited):
        min = float("inf")
        for j in range(self.V):
            if visited[j] == False and min > dist[j]:
                minIndex = j
                min = dist[j]
        return minIndex


    def minimumReverse(self,src,dst):
        dist = [float("inf") for _ in range(self.V)]
        visited = [False]*self.V
        dist[src] = 0

        for _ in range(self.V):
            u = self.selectMinimum(dist,visited)
            visited[u] = True

            for v,w in self.adj[u]:
                if visited[v] == False and dist[v] > dist[u] + w:
                    dist[v] = dist[u]+w
        return dist[dst]

if __name__ == "__main__":
    v = 7
    edge = [[0, 1], [2, 1], [2, 3], [5, 1],[4, 5], [6, 4], [6, 3]]
    g = Graph(v)
    for u,v in edge:
        g.addEdge(u,v)
    print(g.minimumReverse(0,6))

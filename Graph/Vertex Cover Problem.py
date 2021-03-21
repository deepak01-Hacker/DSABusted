
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ Vertex Cover Problem

from collections import defaultdict

class Graph:

    def __init__(self,v):
        self.V = v
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def printVertexCover(self):
        visited = [False]*self.V
        for u in range(self.V):
            if visited[u] == False:
                for v in self.graph[u]:
                    if visited[v] == False:
                        visited[v] = True
                        visited[u] = True
                        break
        print(visited)
        for j in range(self.V):
            if visited[j] :
                print(j,end=" ")
        print()

if __name__ == "__main__":
    g = Graph(3)
    g.addEdge(0,2)
    g.addEdge(1,2)
    g.addEdge(2,1)
    g.addEdge(2,0)
    g.printVertexCover()

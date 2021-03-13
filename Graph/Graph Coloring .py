
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ Graph Coloring -----  :)
#Taste of Greedy ;)

#Undirected Graph

class Graph:

    def __init__(self,V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdge(self,u,v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def Coloring(self):
        result = [-1]*self.V
        result[0] = 0
        available = [False]*self.V

        for u in range(self.V):
            for i in self.adj[u]:
                if result[i] != -1:
                    available[result[i]] = True
            for cr in range(self.V):
                if available[cr] == False:
                    break
            result[u] = cr
            for i in self.adj[u]:
                if result[i] != -1:
                    available[result[i]] = False
        for u in range(self.V):
            print("Vertex " + str(u) +"----->  Color " +str(result[u])) 

if __name__ == "__main__":
    G1 = Graph(5)
    G1.addEdge(0,1)
    G1.addEdge(0,2)
    G1.addEdge(1,2)
    G1.addEdge(1,3)
    G1.addEdge(2,3)
    G1.addEdge(3,4)
    G1.Coloring()

#Hope you understand my simple Code 


#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ Strongly connected Graph
#TArjans #find Bridge

class Graph:
    
    def __init__(self,v):
        self.V = v
        self.graph = []
        self.time = 0

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bridgeUtil(self,u,visited,parent,low,disc):

        visited[u] = True
        low[u] = self.time
        self.time += 1 

        for v in self.graph[u]:
            if visited[v] == False:
                parent[v] = u
                self.bridgeUtil(v,visited,parent,low,disc)

                low[u] = min(low[u],low[v])
                if low[v] > disc[u]:
                    print(u,v)
            elif v != parent[u]:
                low[u] = min(low[u],disc[v])


    def bridge(self):
        visited = [False]*self.V
        disc = [float("inf")] * self.V
        low = [float("inf")] * self.V
        parent = [-1]*self.V
        
        for i in range(self.V):
            if visited[i] == False:
                self.bridgeUtil(i,visited,parent,low,disc)


if __name__ == "__main__":
    g = [[]]



#Hope you understand my simple Code 

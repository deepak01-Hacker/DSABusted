
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ Check whether a given graph is a Bipartite
#

def isBipartite(graph):
    V = len(graph)
    setColor = [-1] * V
    setColor[0] = 1
    queue.append(0)
    while(queue):
        u = queue.pop(0)
        if graph[u][u] == 1:
            return False
        for v in range(V):
            if graph[u][v] == 1 and setColor[v] == -1:
                setColor[v] = 1-setColor[u]
                queue.append(v)
            elif graph[u][v] == 1 and setColor[u] == setColor[v]:
                return False
    return True


if __name__ == "__main__":
    graph = [[]] #adjancyMAtrix
    print(isBipartite(graph))

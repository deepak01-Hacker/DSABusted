
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ Prim's  Algorithm -------
import sys

def printMST(parent,graph):
    print("EDGES    Weight")
    print()
    for i in range(1,len(parent)):
        print(str(parent[i])+" --- "+str(i)+"   "+str(graph[parent[i]][i]))


def minimumDist(dist,visited):
    min_ = 999999999
    for i in range(0,len(dist)):
        if dist[i]<min_ and visited[i] == False:
            min_ = dist[i]
            minIndex = i
    return minIndex


def primsMST(graph):
    V = len(graph)
    parent = [-1]*V
    dist = [999999999]*V
    visited = [False]*V
    dist[0] = 0

    for _ in range(V):
        
        u = minimumDist(dist,visited)
        visited[u] = True

        for v in range(V):
            if graph[u][v] > 0 and visited[v] == False and dist[v] > graph[u][v]:
                dist[v] = graph[u][v]
                parent[v] = u
    
    printMST(parent,graph)


if __name__ == "__main__":
    graph = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 
    
    primsMST(graph)

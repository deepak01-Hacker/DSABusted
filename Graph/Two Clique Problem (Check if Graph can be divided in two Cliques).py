
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ Two Clique Problem (Check if Graph can be divided in two Cliques)
# Hint : Make unpair to pair and pair to unpair
# 

def isPossibleToClique(graph,src,color):
    V = len(graph)
    color[src] = 1
    queue = []
    queue.append(src)
    while(queue):
        u = queue.pop(0)
        for v in range(V):
            if graph[u][v] and color[v] == -1:
                color[v] = 1-color[u]
                queue.append(v)
            elif graph[u][v] and color[v] == color[u]:
                return False
    return True

def Biapertite(G):
    V = len(G)
    GC = [[None] * V for i in range(V)] 
    for i in range(V): 
        for j in range(V): 
            GC[i][j] = not G[i][j] if i != j else 0
    graph = GC
    color = [-1]*len(graph)
    for u in range(len(graph)):
        if color[u] == -1:
            if isPossibleToClique(graph,u,color) == False:
                return False
    return True


if __name__ == "__main__":
    graph = [[0, 1, 1, 1, 0],  
            [1, 0, 1, 0, 0],  
            [1, 1, 0, 0, 0],  
            [0, 1, 0, 0, 1], 
            [0, 0, 0, 1, 0]] 
    print(Biapertite(graph))

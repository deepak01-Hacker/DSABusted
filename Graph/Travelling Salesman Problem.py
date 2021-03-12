
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ Travelling Salesman  :)
#Taste of MST ;)


infinte = 99999999



def minimumDist(visited,dist):
    min = infinte
    for i in range(len(dist)):
        if visited[i] == False and dist[i] < min:
            min = dist[i]
            minIndex = i
    return minIndex

def primsALgo(graph,startPoint):
    V = len(graph)
    dist = [infinte for _ in range(V)]
    parent = [-1] *V
    visited = [False]*V
    dist[startPoint] = 0

    for _ in range(V):

        u = minimumDist(visited,dist)
        visited[u] = True
        for v in range(V):
            if graph[u][v] > 0 and dist[v] == False and dist[v] < graph[u][v]:
                dist[v] = graph[u][v]






if __name__ == "__main__":
    graph = []               #as you want to given there is [Adjancy Matrix] 
    startPoint = 0           # you can also add starting poing in graph Hamaltional something like that ;)
    MSt = primsALgo(graph,startPoint)   #you can print this MST your choice but as parent[i] -- i 

#Hope you understand my simple Code 

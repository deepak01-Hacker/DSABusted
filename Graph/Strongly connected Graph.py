
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ Strongly connected Graph
#TArjans 
#Kosaraju's
#DAG directed Acyclic Graph


def reverseGraph(V,graph):
    g = [[]for _ in range(V)]
    for u in range(len(graph)):
        for v in range(len(graph[u])):
            g[graph[u][v]].append(u)
    return g

def dfs(u,visited,graph,stack):
    visited[u] = True
    for v in graph[u]:
        if visited[v] == False:
            dfs(v,visited,graph,stack)
    stack.append(u)

def dfs2(u,graph,visited):
    visited[u] = True
    for v in graph[u]:
        if visited[v] == False:
            dfs2(v,graph,visited)


def Kosaraju(V,graph):
    #steps to solve this 
    #1.DFS
    #2.REverse
    #3.DFS
    stack = []
    visited = [False]*V
    for u in range(V):
        if visited[u] == False:
            dfs(u,visited,graph,stack)

    visited = [False]*V
    graph = reverseGraph(V,graph)
    StronglyConnecteCommponents = 0
    while(stack):
        curr = stack.pop()
        if visited[curr] == False:
            StronglyConnecteCommponents += 1
            dfs2(curr,graph,visited)

    return StronglyConnecteCommponents

if __name__ == "__main__":
    #0 1 2 3 4
    #1 2 0 0 3
    graph = [[2,3],[0],[1],[4],[]]
    print(Kosaraju(5,graph))

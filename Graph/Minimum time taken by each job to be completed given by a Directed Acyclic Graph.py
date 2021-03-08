
#let's begin and end this life .................. with terror ;)
#Pythonist



def dfs(graph,u,result,unitTime,visited):
    result[u] = unitTime
    visited[u] = True
    for v in graph[u]:
        if visited[v] == False :
            dfs(graph,v,result,unitTime+1,visited)



def minimumUnitTime(graph,N,E):
    result = [10**2 for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    for u in range(1,N+1):
        if visited[u] == False:
            dfs(graph,u,result,1,visited)
    result.pop(0)
    return result



if __name__ == "__main__":
    #first of all this is A DAG means Directed ACyclic Graph
    graph = [[],[2],[3,4,5],[6],[6],[7],[],[]]
    N = 7 # len(graph)-1
    E = 7
    print(minimumUnitTime(graph,N,E))

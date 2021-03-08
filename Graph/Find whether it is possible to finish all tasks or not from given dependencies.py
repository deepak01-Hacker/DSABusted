
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
# 

def detectCycleUtil(adj,u,visited):
    if visited[u] == 1:
        return True
    if visited[u] == 2:
        return False
    visited[u] = 1
    for v in adj[u]:
        if detectCycleUtil(adj,v,visited):
            return True
    visited[u] = 2
    return False


def detectCycle(adj,n):

    visited = [0 for _ in range(n)]
    
    for u in range(n):
        if visited[u] == 0 and detectCycleUtil(adj,u,visited):
            return True
    return False

def checkCAnWEAllotTask(adj,n):
    if detectCycle(adj,n):
        return False
    return True


if __name__ == "__main__":
    graph = [[1,0],[0,1]]
    n = 2
    adj = [[] for _ in range(n)]
    for pair in graph:
        adj[pair[0]].append(pair[1])
    print(checkCAnWEAllotTask(adj,n))



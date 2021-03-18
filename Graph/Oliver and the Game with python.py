
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ Oliver and the Game
#Topological Sort

def dfs(u,visited,mat,stack,stack2):
    visited[u] = True
    stack2.append(u)
    for v in mat[u]:
        if visited[v] == False:
            dfs(v,visited,mat,stack,stack2)
    stack.append(u)

def dfs2(u,visited,mat):
    visited[u] = True


def sort(graph,n,queries):
    mat = [[] for _ in range(n+1)]
    for u,v in graph:
        mat[u].append(v)
        mat[v].append(u)
    
    stack = []
    stack2 = []
    visited = [False]*(n+1)
    for u in range(1,(n+1)):
        if visited[u] == False:
            dfs(u,visited,mat,stack,stack2)
    print(stack)
    first = stack.index(queries[1])
    nexts = stack.index(queries[2])
    first1 = stack2.index(queries[1])
    nexts1 = stack2.index(queries[2])
    if first > nexts and first1 < nexts1 and queries[0] == 0:
        return "YES"
    elif nexts > first and nexts1 < first1 and queries[0] == 1:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    n = 9
    graph = [[1 ,2],[1 ,3],[2 ,6],[2, 7],[6, 9],[7 ,8],[3, 4],[3, 5]]
    print(sort(graph,n,[1,9,1]))

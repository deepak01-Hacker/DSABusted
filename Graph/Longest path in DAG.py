
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ Longest path in GIven Graph
#Here we find longest distance from source if we want to find shortest distance from source then we have to only mulitply 
# edge weight with -1 and process it and after multiply that with  -1 again .............. yeah our answer is ready


def dfs(u):
    global visited,adj,Stack
    visited[u] = True
    for i in adj[u]:
        if visited[i[0]] == False:
            dfs(i[0])
    Stack.append(u)


def longestPath(s):
    global adj,Stack,visited ,V
    distances = [-float("inf") for _ in range(V)]
    for u in range(V):
        if visited[u] == False:
            dfs(u)
    
    distances[s] = 0
    while(Stack):
        u = Stack.pop()
        if distances[u] != -float("inf"):
            for i in adj[u]:
                if distances[i[0]] < distances[u] + i[1]:
                    distances[i[0]] = distances[u]+i[1]
    print(distances) #here is  



 #-------------------- this Code from GFG ------------- \/ ---
if __name__ == "__main__":
    V, Stack, visited = 6, [], [False for i in range(7)]
    adj = [[] for i in range(7)]
    
    adj[0].append([1, 5])
    adj[0].append([2, 3])
    adj[1].append([3, 6])
    adj[1].append([2, 2])
    adj[2].append([4, 4])
    adj[2].append([5, 2])
    adj[2].append([3, 7])
    adj[3].append([5, 1])
    adj[3].append([4, -1])
    adj[4].append([5, -2])
 
    s = 1
    print("Following are longest distances from source vertex ",s)
    longestPath(s)


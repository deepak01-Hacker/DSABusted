
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ m coloring Problem




# ---------------------- BackTracking ---------------------------------


class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]\
                              for row in range(vertices)]
 
    # A utility function to check 
    # if the current color assignment
    # is safe for vertex v
    def isSafe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True
     
    # A recursive utility function to solve m
    # coloring  problem
    def graphColourUtil(self, m, colour, v):
        if v == self.V:
            return True
 
        for c in range(1, m + 1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColourUtil(m, colour, v + 1) == True:
                    return True
                colour[v] = 0
 
    def graphColouring(self, m):
        colour = [0] * self.V
        if self.graphColourUtil(m, colour, 0) == None:
            return False
 
        # Print the solution
        print "Solution exist and Following 
                  are the assigned colours:"
        for c in colour:
            print c,
        return True
 
# Driver Code
g = Graph(4)
g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m = 3
g.graphColouring(m)











#------------------------- Naive Approach from GFG ------------------ simple 

# Number of vertices in the graph
# define 4 4
 
# check if the colored
# graph is safe or not
def isSafe(graph, color):
   
    # check for every edge
    for i in range(4):
        for j in range(i + 1, 4):
            if (graph[i][j] and color[j] == color[i]):
                return False
    return True
 
# /* This function solves the m Coloring
# problem using recursion. It returns
# false if the m colours cannot be assigned,
# otherwise, return true and prints
# assignments of colours to all vertices.
# Please note that there may be more than
# one solutions, this function prints one
# of the feasible solutions.*/
def graphColoring(graph, m, i, color):
   
    # if current index reached end
    if (i == 4):
 
        # if coloring is safe
        if (isSafe(graph, color)):
 
            # Prthe solution
            printSolution(color)
            return True
        return False
 
    # Assign each color from 1 to m
    for j in range(1, m + 1):
        color[i] = j
 
        # Recur of the rest vertices
        if (graphColoring(graph, m, i + 1, color)):
            return True
        color[i] = 0
    return False
 
# /* A utility function to prsolution */
def printSolution(color):
    print("Solution Exists:" " Following are the assigned colors ")
    for i in range(4):
        print(color[i],end=" ")
 
# Driver code
if __name__ == '__main__':
   
    # /* Create following graph and
    # test whether it is 3 colorable
    # (3)---(2)
    # | / |
    # | / |
    # | / |
    # (0)---(1)
    # */
    graph = [
        [ 0, 1, 1, 1 ],
        [ 1, 0, 1, 0 ],
        [ 1, 1, 0, 1 ],
        [ 1, 0, 1, 0 ],
    ]
    m = 3 # Number of colors
 
    # Initialize all color values as 0.
    # This initialization is needed
    # correct functioning of isSafe()
    color = [0 for i in range(4)]
 
    if (not graphColoring(graph, m, 0, color)):
        print ("Solution does not exist")








#-----------------------------------------------------------------
class Graph:

    def __init__(self,v):
        self.V = v
        self.adj = [[] for _ in range(self.V)]

    def addEdge(self,u,v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def coloring(self,m):
        color = [1]*self.V
        visited = [False]*self.V
        maxColor = 1
        for u in range(self.V):
            if visited[u] == False:
                visited[u] = True
                queue = []
                queue.append(u)
                while(queue):
                    u = queue.pop(0)
                    for v in self.adj[u]:
                        if color[u] == color[v]:
                            color[v] += 1
                        maxColor = max(maxColor,color[u],color[v])
                        if maxColor > m:
                            return False
                        if visited[v] == False:
                            visited[v] = True
                            queue.append(v)
        return True

if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(0,3)
    g.addEdge(1,2)
    g.addEdge(2,3)
    print(g.coloring())



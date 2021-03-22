
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ Count Triangle in Graph

def countTriangle(graph,isDirected):
    nodes = len(graph)
    count_triangle = 0

    for i in range(nodes):
        for j in range(nodes):
            for k in range(nodes):
                if i != j and i != k and j != k and graph[i][j] and graph[j][k] and graph[k][i]:
                    count_triangle += 1
    if isDirected:
        return count_triangle//3 # we devide bcz the count 1 triangle 3 time
    return count_triangle // 6  


if __name__ == "__main__":
    graph = [[0,1,1,0],
             [1,0,1,1],
             [1,1,0,1],
             [0,1,1,0]]
    print("Triangle in Graph :) - "+str(countTriangle(graph,False)))

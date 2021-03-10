
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ count total number of spanning Tree in Graph  -------
#@ kirchoff's 

#I am Wrong here ............. ;)


def countSpanningTRee(adjMat,V):
    degreeMAtrix = [sum(adjMat[i]) for i in range(V)]
    for diagonal in range(V):
        adjMat[diagonal][diagonal] = degreeMAtrix[diagonal]
    for row in range(V):
        for col in range(V):
            if adjMat[row][col] == 1:
                adjMat[row][col] = -1
    
    C = V-2
    R = V-2
    ans = adjMat[R][C] * adjMat[R+1][C+1]
    ans -= adjMat[R][C+1]*adjMat[R+1][C]
    
    return ans

    


if __name__ == "__main__":
    graph = [[1,3],[1,4],[2,3],[2,4],[3,4]]
    V = 4
    adjMat = [[0 for _ in range(V)] for _ in range(V)]
    for edge in graph:
        adjMat[edge[0]-1][edge[1]-1] = 1
        adjMat[edge[1]-1][edge[0]-1] = 1
    print(countSpanningTRee(adjMat,V))


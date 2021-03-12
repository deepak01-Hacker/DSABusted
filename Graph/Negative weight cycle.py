
#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
#  words of deepak


#fun fact is that !

#@ Bellman Ford Algorithm for detecting negative weight cycle

class Solution:
    def isNegativeWeightCycle(self,n,edges):
        dist = [float('inf') for _ in range(n)]
        dist[0] = 0

        for _ in range(n-1):
            for u,v,w in edges:
                if dist[u] !=  float('inf') and dist[u]+w < dist[v]:
                    dist[v] = dist[u]+w
        #print(dist)
        for u,v,w in edges:
            if dist[u] !=  float('inf') and dist[u]+w < dist[v]:
                return False
        return True
        #printMST(i,dist[i])

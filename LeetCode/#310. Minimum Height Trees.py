class Solution(object):
    

    def util(self,graph,i):
        visited = set()

        q = []
        q.append([i,0])

        hight = 0

        while(q):
            root,level = q.pop(0)
            visited.add(root)

            for vert in graph[root]:

                if vert not in visited:
                    q.append([vert,level+1])
            hight = max(hight,level)

        return hight+1 

    def minimumHeights(self,edges,n):

        graph = {}

        for i,j in edges:
            if i in graph.keys():
                graph[i].append(j)
            else:
                graph[i] = []
                graph[i].append(j)

            if j in graph.keys():
                graph[j].append(i)
            else:
                graph[j] = []
                graph[j].append(i)

        res = []
        mini = n+1

        for i in range(n):
            hight = self.util(graph,i)

            #print(hight)

            if mini > hight:
                res = []
                res.append(i)
                mini = hight

            elif mini == hight:
                res.append(i)

        return res

    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
        return self.minimumHeights(edges,n)
        

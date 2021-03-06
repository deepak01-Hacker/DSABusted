class Solution(object):
    
    def BFSUtil(self,graph,v,checker):
        queue = []
        queue.append(v)
        while(queue):
            u = queue.pop()
            checker.add(u)
            for i in graph[u]:
                if i not in checker:
                    queue.append(i)
            
        
    
    def makeConnected(self, n, connections):
        graph = [[] for _ in range(n)]
        for i in range(len(connections)):
            graph[connections[i][0]].append(connections[i][1])
            graph[connections[i][1]].append(connections[i][0])
    
        cycleCount = 0
        checker = set()
        if len(connections) < n-1:
            return -1
        
        for v in range(n):
            if v not in checker:
                self.BFSUtil(graph,v,checker)
                cycleCount += 1
        
        return cycleCount-1


        
            

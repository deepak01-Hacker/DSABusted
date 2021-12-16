class Solution(object):
    
    def __init__(self):
        self.adj = {}
        self.degree = []
        self.V = 0
        
    

    

    def findMinHeightTrees(self, V, edges):
        if V == 1:
            return [0]
        self.degree = [0]*V
        self.V = V
        
        for i,j in edges:
            self.degree[i] += 1
            self.degree[j] += 1
            if i in self.adj.keys():
                self.adj[i].append(j)
            else:
                self.adj[i] = []
                self.adj[i].append(j)

            if j in self.adj.keys():
                self.adj[j].append(i)
            else:
                self.adj[j] = []
                self.adj[j].append(i)
    
        from Queue import Queue
        q = Queue()

        # First enqueue all leaf nodes in queue
        for i in range(self.V):
            if self.degree[i] == 1:
                q.put(i)

        # loop until total vertex remains less than 2
        while(self.V > 2):
            p = q.qsize()
            self.V -= p
            for i in range(p):
                t = q.get()

                # for each neighbour, decrease its degree and
                # if it become leaf, insert into queue
                for j in self.adj[t]:
                    self.degree[j] -= 1
                    if self.degree[j] == 1:
                        q.put(j)

        #  Copying the result from queue to result vector
        res = list()
        while(q.qsize() > 0):
            res.append(q.get())

        return res

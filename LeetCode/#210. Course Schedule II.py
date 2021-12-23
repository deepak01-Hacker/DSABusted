class Solution(object):

    def dfs(self,graph,u,visited,ans):
        if visited[u] == 1:
            return True
        elif visited[u] == 2:
            return False

        visited[u] = 1
        for v in graph[u]:
            if self.dfs(graph,v,visited,ans):
                return True
        visited[u] = 2
        ans.append(u)
        return False




    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        graph = [[] for _ in range(numCourses)]

        for u,v in prerequisites:
            graph[u].append(v)


        visited = [0]*numCourses
        ans = []

        for u in range(0,numCourses):

            if self.dfs(graph,u,visited,ans):
                return []
            
        return ans
        

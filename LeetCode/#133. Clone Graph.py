"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if node == None:
            return None
        
        q = []
        new = Node(node.val)

        q.append(node)
        map = {}
        map[new.val] = new


        visited = set()

        while(q):

            node = q.pop()

            if node.val not in visited:
                visited.add(node.val)

                for i in node.neighbors:
                    if i.val not in map:
                        map[i.val] = Node(i.val)
                    
                    q.append(i)

                    map[node.val].neighbors.append(map[i.val])
        #print(new.val)

        return new    

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if node is None:
            return Node(neighbors=[])
        queue = []
        map = {}

        cloneVAl = Node(node.val)
        map[node] = cloneVAl

        queue.append(node)
        while(queue):
            u = queue.pop(0)
            v = [add for add in u.neighbors]
            for add in v:
                try:
                    map[add] = map[add]
                except:
                    new = Node(add.val)
                    map[add] = new
                    queue.append(add)
                map[u].neighbors.append(map[add])
        return map[node]
        

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    
    def connect(self,root):
        
        store = [root]

        while(root):
            tempNode = root

            while(tempNode):

                if (tempNode.left and tempNode.right):
                    tempNode.left.next = tempNode.right
                    tempNode.right.next = self.getNextNode(tempNode.next)

                elif (tempNode.left or tempNode.right):
                    self.getNextNode(tempNode).next = self.getNextNode(tempNode.next)

                tempNode = tempNode.next

            root = self.getNextNode(root)
        
        return store[0]


    def getNextNode(self,root):
        if root is None:
            return None

        if root.left :
            return root.left

        if root.right:
            return root.right

        return self.getNextNode(root.next)

        

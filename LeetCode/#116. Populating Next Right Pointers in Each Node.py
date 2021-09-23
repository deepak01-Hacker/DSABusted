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
    def utilConnect(self,root):
        if root is None:
            return 
        stack = []
        
        stack.append(root)
        
        while(stack):
            length = len(stack)
            
            prev = None
            while(length):
                root = stack.pop(0)
                
                if root.left:
                    stack.append(root.left)
                
                if root.right:
                    stack.append(root.right)
                
                if prev != None:
                    prev.next = root
                prev = root
                length -= 1
            
                
        
        
    
    def connect(self, root):
        
        self.utilConnect(root)
        return root
        

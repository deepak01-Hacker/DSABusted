# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    
    def util(self,root,depth):
        
        if root is None:
            return 0
        
        return max(depth,self.util(root.left,depth+1),self.util(root.right,depth+1))
    
    def maxDepth(self, root):
        if root is None:
            return 0
        
        return self.util(root,1)
        
        

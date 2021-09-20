# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def util(self,root,tr):
        
        if root is None:
            return False
        
        if root and not root.left and not root.right and tr-root.val == 0:
            return True
            
        
        return self.util(root.left,tr-root.val) or self.util(root.right,tr-root.val)
        
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        return self.util(root,targetSum)
        

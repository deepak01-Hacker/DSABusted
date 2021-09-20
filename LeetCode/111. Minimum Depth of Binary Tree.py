# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def depthUtil(self,root):
        if root is None:
            return 0
        
        ldepth = self.depthUtil(root.left)
        rdepth = self.depthUtil(root.right)
        
        if ldepth != 0 and rdepth != 0:
            return min(ldepth+1,rdepth+1)
        else:
            return max(ldepth+1,rdepth+1)
            
            
    
    def minDepth(self, root):
        return self.depthUtil(root)
        

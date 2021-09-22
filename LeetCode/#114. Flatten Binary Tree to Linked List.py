# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution(object):
    def preOrder(self,root,pre):
        if root is None:
            return None
        
        pre.append(root)
        
        self.preOrder(root.left,pre)
        self.preOrder(root.right,pre)
    
    
    def flatten(self, root):
        pre = [] 
        self.preOrder(root,pre)
        
        for i in range(len(pre)):
            if (i+1) < len(pre):
                pre[i].right = pre[i+1]
            pre[i].left = None
            
        return root
        

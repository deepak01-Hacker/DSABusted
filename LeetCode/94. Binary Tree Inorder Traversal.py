

#----------------------- Recursive Code- -----------------------------------



# Definition for a binary tree node.



class Solution(object):
    def inoUtil(self,root,inorder):
        if root is None:
            return None
        
        self.inoUtil(root.left,inorder)
        inorder.append(root.val)
        self.inoUtil(root.right,inorder)
        
    
    def inorderTraversal(self, root):
        
        inorder = []
        self.inoUtil(root,inorder)
        
        return inorder
        

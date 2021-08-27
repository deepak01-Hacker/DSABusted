

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
    
    
    #--------------------- With -Stack ---------------------
    
    

class Solution(object):
        
    def inorderTraversal(self, root):
        if root is None:
            return []
        
        inorder = []
        stack = []
        
        while(True):
            if root:
                stack.append(root)
                root = root.left
                
            elif stack:
                inorder.append(stack[-1].val)
                root = stack[-1].right
                stack.pop()
            else:
                break
                
        return inorder
        

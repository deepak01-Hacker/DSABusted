
class Solution(object):
    
    def util(self,root,min,max):
        if root is None:
            return True
        
        if root.val <= min or root.val >= max:
            return False
        
        return self.util(root.left,min,root.val) and self.util(root.right,root.val,max)
    
    def isValidBST(self, root):
        return self.util(root,-2**32,(2**32))
        
        
        

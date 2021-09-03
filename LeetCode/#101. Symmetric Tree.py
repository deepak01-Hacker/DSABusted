
class Solution(object):
    
    def isMirror(self,root1,root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        
        if root1.val == root2.val:
            return self.isMirror(root1.left,root2.right) and self.isMirror(root1.right,root2.left)
        
        return False
    
    def isSymmetric(self, root):
        return self.isMirror(root.left,root.right)
        
        

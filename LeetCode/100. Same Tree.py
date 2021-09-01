
class Solution(object):
    def isSameTree(self, p, q):
        
        if p is None and q is None:
            return True
        
        if p is None:
            return False
        elif q is None:
            return False
        
        if p.val == q.val :
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False
            
        
        
        

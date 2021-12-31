# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def util(self,root,ans):
        if root is None:
            return []
        elif root and root.left == None and root.right == None:
            return [root.val,root.val]
        
        lr = self.util(root.left,ans)
        rr = self.util(root.right,ans)
        
        temp = []
        
        if lr and rr:
        
            mins_ = min(min(lr),min(rr)) 
            maxs_ = max(max(lr),max(rr))
        else:
            mins_ = min(lr) if lr else min(rr)
            maxs_ = max(lr) if lr else max(rr)
        
        ans[0] = max(ans[0],abs(mins_-root.val),abs(maxs_-root.val))
        
        temp.append(min(mins_,root.val))
        temp.append(max(maxs_,root.val))        
        return temp
        
    def maxAncestorDiff(self, root):
        ans = [0]
        
        self.util(root,ans)
        
        return ans[0]

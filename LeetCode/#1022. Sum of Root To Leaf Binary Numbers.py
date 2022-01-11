# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def util(self,root,number,ans):
        if root is None:
            return 
        if root and root.left is None and root.right is None :
            number += str(root.val)
            
            ans[0] += int(number,2)
        
        self.util(root.left,number+str(root.val),ans)
        self.util(root.right,number+str(root.val),ans)

    
    def sumRootToLeaf(self, root):
        
        ans = [0]
        
        self.util(root,"",ans)
        
        return ans[0]
        

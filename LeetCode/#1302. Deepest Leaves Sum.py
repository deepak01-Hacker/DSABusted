# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self,root,lvl,util):
        if root is None:
            return 
        
        if util[1] == lvl:
            util[0] += root.val
        elif util[1] < lvl:
            util[1] = lvl
            util[0] = root.val
        
        self.solve(root.left,lvl+1,util)
        self.solve(root.right,lvl+1,util)
        
        
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        util = [0,-1]
        self.solve(root,0,util)
        return util[0]
        
        

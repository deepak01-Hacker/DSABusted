# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        
        if root is None:
            return TreeNode(val)
        
        head = root
        
        prev = None
        
        while(root):
            prev = root
            if root.val < val:
                root = root.right
            else:
                root = root.left
        if prev.val < val:
            prev.right = TreeNode(val)
        else:
            prev.left = TreeNode(val)
        return head
        

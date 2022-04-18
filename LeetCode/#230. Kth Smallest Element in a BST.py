# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self,root,ino):
        if root is None:
            return 
        self.inorder(root.left,ino)
        ino.append(root.val)
        self.inorder(root.right,ino)
        
    def kthSmallest(self, root, k):
        
        ino = []
        self.inorder(root,ino)
        return ino[k-1]

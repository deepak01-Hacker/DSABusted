# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def merge(self,root1,root2):
        if root1 is None and root2 is None:
            return None

        sum = 0 if root1 is None else root1.val
        sum += 0 if root2 is None else root2.val

        newNode = TreeNode(sum)

        newNode.left = self.merge(root1.left if root1 else None,root2.left if root2 else None)

        newNode.right = self.merge(root1.right if root1 else None,root2.right if root2 else None)

        return newNode

    
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        return self.merge(root1,root2)
        

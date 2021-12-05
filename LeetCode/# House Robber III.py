# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def util(self,root):
        if root is None:
            return [0,0]  #prev ,

        l = self.util(root.left)
        r = self.util(root.right)

        newAdj = l[0]+r[0]+root.val

        newPrev = max(l[0],l[1])+max(r[1],r[0])

        #print(l,r,root.val)

        return [newPrev,newAdj]

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = self.util(root)
        return max(ans)
        

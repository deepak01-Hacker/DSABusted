# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    
    def maxPathSumUtil(self,root,ans):
    
        if root is None:
            return 0

        left = self.maxPathSumUtil(root.left,ans)
        right = self.maxPathSumUtil(root.right,ans)

        ans[0] = max(ans[0],left+right+root.val,left+root.val,right+root.val,root.val)

        return max(root.val+left,right+root.val,root.val)


    def maxPathSum(self, root):
        ans = [-1001]
        self.maxPathSumUtil(root,ans)
        
        return ans[0]
        
        

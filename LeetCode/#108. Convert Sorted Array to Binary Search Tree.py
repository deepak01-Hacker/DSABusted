# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def buildBST(self,nums):
        if nums == []:
            return None
        
        mid = len(nums)//2

        root = TreeNode(nums[mid])
        root.left = self.buildBST(nums[:mid])
        root.right = self.buildBST(nums[mid+1:])

        return root

    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.buildBST(nums)

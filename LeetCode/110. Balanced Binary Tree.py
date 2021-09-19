# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution(object):
    def checkBalanced(self,root,ans):
        if root is None:
            return 0
        
        lhight = self.checkBalanced(root.left,ans)
        rhight = self.checkBalanced(root.right,ans)
        
        print(abs(lhight-rhight))
        
        if abs(lhight-rhight) <= 1 :
            return max(lhight,rhight) + 1
        else:
            ans[0] = False
            return -3
    
    
    def isBalanced(self, root):
        #print(self.checkBalanced(root))
        ans = [True]
        self.checkBalanced(root,ans)
        return ans[0]
        

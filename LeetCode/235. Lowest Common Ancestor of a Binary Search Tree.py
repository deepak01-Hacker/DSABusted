# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def depth(self,root,ans):
        if root is None:
            return None
        #print(ans[2],root.val)
        #ans[2] = min(ans[2],int(root.val))
        
        mid = root.val
        #print(ans[2],root.val)
        if mid > ans[0] and mid > ans[1]:
            return self.depth(root.left,ans)
        elif (root.val < ans[0] and root.val < ans[1] ):
            return self.depth(root.right,ans)
        else:
            ans[2] = mid
        
    
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return 0
        ans = [int(10**9),int(p.val),int(q.val)]
        ans.sort()
        self.depth(root,ans)
        return TreeNode(ans[-1])
        

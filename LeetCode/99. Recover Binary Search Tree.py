# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        prev = [None]
        res = []

        self.util(root,prev,res)
        
        if len(res) == 1:
            res.append(prev[0])
            
        if len(res) == 2:
            res[0].val,res[1].val = res[1].val,res[0].val
            
            return root
        

    def util(self,root,prev,res):
        if root is None:
            return
        self.util(root.left,prev,res)

        #print(prev[0].val)
        if prev[0] and prev[0].val > root.val :
            if res == []:
                res.append(prev[0])
                res.append(root)

        if res and res[-1].val > root.val:
            res[-1] = root
            
        prev[0] = root
        #print(prev[0].val)
        self.util(root.right,prev,res)

            

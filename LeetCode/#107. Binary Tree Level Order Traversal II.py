# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        if root is None:
            return []
        res = []
        
        stack = []
        stack.append(root)
        
        
        while(True):
            
            if stack :
                
                lengthOfrow = len(stack)
                res.append([])
                
                while(lengthOfrow>0):
                    
                    root = stack.pop(0)
                    res[-1].append(root.val)
                    
                    if root.left:
                        stack.append(root.left)
                        
                    if root.right:
                        stack.append(root.right)
                    

                    lengthOfrow -= 1
            else:
                break
                
        return res[::-1]
        

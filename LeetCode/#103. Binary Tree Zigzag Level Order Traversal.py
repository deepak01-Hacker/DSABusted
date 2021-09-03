# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        
        if root is None:
            return []
    
        res = []
        
        queue = [root]
        level = 0
    
        
        while(True):
            
            if queue :
                
                lengthOfrow = len(queue)
                res.append([])
                
                level += 1
                
                while(lengthOfrow>0):
                    
                    root = queue.pop(0)
                    
                    if level%2 != 0:
                        
                        res[-1].append(root.val)
                    else:
                        res[-1].insert(0,root.val)
                    
                    if root.left:
                        queue.append(root.left)
                        
                    if root.right:
                        queue.append(root.right)
                    
                    lengthOfrow -= 1
            else:
                break
        return res
        

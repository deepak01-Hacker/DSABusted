# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorder(root,ino):
        if root is None:
            return
        inorder(root.left,ino)
        ino.append(root.val)
        inorder(root.right,ino)
        
class Solution(object):
    
    
    def getAllElements(self, root1, root2):
        ans = []
        
        ino1 = []
        inorder(root1,ino1)
        
        ino2 = []
        inorder(root2,ino2)
        
        i = 0
        j = 0
        
        while(i < len(ino1) and j < len(ino2)):
            if ino1[i] < ino2[j]:
                ans.append(ino1[i])
                i += 1
            else:
                ans.append(ino2[j])
                j += 1
        while(i < len(ino1)):
            ans.append(ino1[i])
            i += 1
        
        while(j < len(ino2)):
            ans.append(ino2[j])
            j += 1
        
        return ans

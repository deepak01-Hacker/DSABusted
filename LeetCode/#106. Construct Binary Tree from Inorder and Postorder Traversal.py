# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructTree(self,inorder,postorder):

        if inorder == []:
            return None


        root = TreeNode(postorder[-1])

        isValid = False
        for i in range(len(inorder)):
            if inorder[i] == postorder[-1]:
                isValid = True
                break

        if isValid:
            postorder.pop()
        else:
            return None

        #print(ino)

        root.right = self.constructTree(inorder[i+1:],postorder)

        root.left = self.constructTree(inorder[:i],postorder)




        return root
    
    def buildTree(self, inorder, postorder):
        
        return self.constructTree(inorder,postorder)
        
        

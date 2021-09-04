# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructTree(self,inorder,preorder):

        if inorder == []:
            return None


        root = TreeNode(preorder[0])

        isValid = False
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                isValid = True
                break

        if isValid:
            preorder.pop(0)
        else:
            return None

        #print(inorder)


        root.left = self.constructTree(inorder[:i],preorder)
        root.right = self.constructTree(inorder[i+1:],preorder)




        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.constructTree(inorder,preorder)
        

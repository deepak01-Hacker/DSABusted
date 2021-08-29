# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructTrees(self,start,end):

        list = []


        if (start > end) :

            list.append(None)
            return list

        for i in range(start, end + 1):

            leftSubtree = self.constructTrees(start, i - 1)

            rightSubtree = self.constructTrees(i + 1, end)


            for j in range(len(leftSubtree)) :
                left = leftSubtree[j]
                for k in range(len(rightSubtree)):
                    right = rightSubtree[k]
                    node = TreeNode(i)   
                    node.left = left    
                    node.right = right    
                    list.append(node)  

        return list
    def preorder(self,root,k) :
 
        if (root != None) :

            k.append(root.val)
            self.preorder(root.left,k)
            self.preorder(root.right,k)

    def generateTrees(self, n):
        
        ans = self.constructTrees(1,n)
        return ans
            
        
        
    
        

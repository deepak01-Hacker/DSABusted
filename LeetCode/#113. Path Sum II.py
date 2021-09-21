# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    
    def util(self,root,tr,path,ans):
        
        if root and root.left == None and root.right == None :
            if tr-root.val == 0:
                path.append(root.val)
                #print(path)
            
                tempPath = tuple(i for i in path)
                #print(tempPath)
                ans.append(tempPath)
                path.pop()
            return 
            
        if root is None:
            return None
        
        path.append(root.val)
        
        self.util(root.left,tr-root.val,path,ans)
        
        self.util(root.right,tr-root.val,path,ans)
        
        path.pop()
        
    
        

    
    def pathSum(self, root, targetSum):
        ans = []
        self.util(root,targetSum,[],ans)
        #print(ans)
        return ans



"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution(object):
    
    def util(self,root,number,ans):
        if root is None:
            return
        
        if root and root.left is None and root.right is None:
            print(root.val)
            number += str(root.val)
            ans[0] += int(number)
            
            #print(ans[0])
            return

        self.util(root.left,number+str(root.val),ans)
        self.util(root.right,number+str(root.val),ans)


    def sumNumbers(self, root):
        ans = [0]
        
        self.util(root,"",ans)
        
        return ans[0]
        

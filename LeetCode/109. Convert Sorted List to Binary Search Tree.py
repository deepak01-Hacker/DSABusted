# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.

# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def midFind(self,head):
        start = head
        fast = head
        prev = None

        while(fast and fast.next != None ):
            prev = start
            start = start.next
            fast = fast.next.next

        prev.next = None
        return start





    def makeTree(self,head):

        if head is None or head.next is None:
            return TreeNode(head.val) if head else None

        mid = self.midFind(head)
        midNext = mid.next
        mid.next = None

        root = TreeNode(mid.val)

        root.left = self.makeTree(head)
        root.right = self.makeTree(midNext)

        return root

    def sortedListToBST(self, head):
        root = self.makeTree(head)
        return root
        
        

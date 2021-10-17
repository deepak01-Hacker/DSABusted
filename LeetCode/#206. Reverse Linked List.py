# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverse(self,head):

        if head is None or head.next is None:
            return head

        newHead = self.reverse(head.next)
        temp = head.next
        temp.next = head
        head.next = None

        return newHead
    
    def reverseList(self, head):
        return self.reverse(head)
        

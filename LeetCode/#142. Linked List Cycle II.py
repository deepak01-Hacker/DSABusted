# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if head == None:
            return head
        
        slow = head
        fast = head.next
        
        while(fast and fast.next and slow != fast):
            slow = slow.next
            fast = fast.next.next
        
        slow = slow.next
        
        while(slow and head and head != slow):
            head = head.next
            slow = slow.next
            
        return slow if head == slow else None
        

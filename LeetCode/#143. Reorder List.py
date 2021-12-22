# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = head
        fast = head
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        
        while(slow):
            currNxt = slow.next
            slow.next = prev
            prev = slow
            
            slow = currNxt
        
        slow = prev
        newHead = head
        
        while(slow and head ):
            hdNxt = head.next
            slwNxt = slow.next
            
            head.next = slow
            slow.next = None
            if hdNxt != slow:
                slow.next = hdNxt
            
            head = hdNxt
            slow = slwNxt
        # 1->4->2->
        
        

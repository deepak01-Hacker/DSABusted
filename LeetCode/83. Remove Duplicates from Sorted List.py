# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        tempHead = head
        
        while(tempHead):
            
            if tempHead.next and tempHead.next.val == tempHead.val:
                tempHead.next = tempHead.next.next
            else:
                tempHead = tempHead.next
            
        return head

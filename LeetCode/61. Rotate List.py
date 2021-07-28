# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        
        stack = []
        
        
        tempHead = head
        while(tempHead):
            stack.append(tempHead)
            tempHead = tempHead.next
            
        if k == 0 or head == None:
            return head
            
        k = k%len(stack)
        
        while(k):
            stack[-1].next = head
            head = stack[-1]
            stack.pop()
            k -= 1
            
        if stack:
            stack[-1].next = None
        return head
            
            
    
        

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        
        if head == None:
            return head
        
        even = head
        evenHead = head
        
        odd = None
        oddHead = None
        
        ct = 1
        head = head.next
        
        while(head != None):
            
            currNext = head.next
            
            if ct %2 == 0:
                evenHead.next = head
                evenHead = evenHead.next
                
                evenHead.next = None
            else:
                if odd == None:
                    odd = head
                    oddHead = head
                else:
                    oddHead.next = head
                    oddHead = oddHead.next
                
                oddHead.next = None
                
            head = currNext
            ct += 1
        evenHead.next = odd
        return even
        
        

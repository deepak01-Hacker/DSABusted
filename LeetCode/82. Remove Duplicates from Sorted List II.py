# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        
        if head == None:
            return head
        
        new = None
        prev = None
        tempHead = head.next

        ite = [head,1]

        while(tempHead):

            currNxt = tempHead.next
            
            if tempHead.val == ite[0].val:
                ite[1] += 1
            else:
                if ite[1] == 1:
                    if prev == None:
                        prev = ite[0]
                        new = ite[0]

                        ite[0].next = None
                    else:
                        prev.next = ite[0]
                        prev.next.next = None
                        
                        prev = ite[0]
                        
                ite = [tempHead,1]

            tempHead = currNxt
            
        if ite[1] == 1:
            if prev == None:
                prev = ite[0]
                new = ite[0]

                ite[0].next = None
            else:
                prev.next = ite[0]
                prev.next.next = None
                
        return new
        

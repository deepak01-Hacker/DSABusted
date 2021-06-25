# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
    
        sortedhead = None
        temp = None
        
        while(l1 and l2):
            if l1.val < l2.val:
                minimum = l1
                l1 = l1.next
            else:
                minimum = l2
                l2 = l2.next
                
            if sortedhead == None:
                temp = minimum
                sortedhead = temp
                
            temp.next = minimum
            temp = temp.next
            
        if l1:
            temp.next = l1
        elif l2:
            temp.next = l2
            
        return sortedhead
            
            
        

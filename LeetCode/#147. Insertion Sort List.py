# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        prev = None
        while(head != None):
            curr = head.next
            head.next = prev
            prev = head
            
            key = head.val
            
            temp = head.next
            prevk = head
            
            while(temp and key < temp.val):
                prevk.val = temp.val
                prevk = temp
                temp = temp.next
                
            prevk.val = key 
            
            head = curr
        
        last = None
        while(prev):
            currNxt = prev.next
            prev.next = last
            last = prev
            
            prev = currNxt
        return last
            

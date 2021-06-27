# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if head == None:
            return None
        
        arr = []

        
        while(head):
            arr.append(head)
            head = head.next
            
        for i in range(0,len(arr)-1,2):
            arr[i],arr[i+1] = arr[i+1],arr[i]
        
        for i in range(0,len(arr)-1):
            arr[i].next = arr[i+1]
        
        arr[-1].next = None
        return arr[0]
      
     
        

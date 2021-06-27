
#----------------------- Heap =================================

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hp

class Solution(object):
    def mergeKLists(self, lists):
        head = None
        tempHead = None

        heap = []
        hp.heapify(heap)
        
        for i in range(len(lists)):
            if lists[i] != None:
                hp.heappush(heap,[lists[i].val,lists[i]])
        
        while(heap):
            popNode = hp.heappop(heap)
            
            if head == None:
                head = popNode[1]
                tempHead = head
            else:
                tempHead.next = popNode[1]
                tempHead = tempHead.next
            
            if popNode[1].next != None:
                hp.heappush(heap,[popNode[1].next.val,popNode[1].next])
            
        return head
            
















# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        head = None
        temp = None
        while(True):
            mini = -1
            for currHead in range(len(lists)):
                if lists[currHead] != None:
                    if mini == -1:
                        mini = currHead

                    elif lists[currHead].val < lists[mini].val:
                        mini = currHead
                        
            if mini == -1:
                if temp == None:
                    return head
                temp.next = None
                return head
            
            if head == None:
                head = lists[mini]
                temp = head
            else:
                temp.next = lists[mini]
                temp = temp.next

            lists[mini] = lists[mini].next

        
        

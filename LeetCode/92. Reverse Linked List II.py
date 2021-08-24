# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):

        if (head and head.next == None) or head == None:
            return head

        tempHead = head
        
        prevleft = None
        
        while(tempHead != None and left > 1):
            prevleft = tempHead
            tempHead = tempHead.next
            left -= 1
        

            
        leftAdd = tempHead
        
        rightPrev = None

        tempHead = head
        
        while(tempHead != None and right > 0):
            right -= 1
            rightPrev = tempHead
            tempHead = tempHead.next
        
        #print(rightPrev.val)
            
        if prevleft == rightPrev:
            return head
        
        tempHead = leftAdd
        rrNext = rightPrev.next    

        prev = None

        #print(prevleft.val,leftAdd.val,rightPrev.val)
        
        while(tempHead and tempHead != rrNext):
            #print(tempHead.val)
            currNext = tempHead.next
            #print(currNext.val)
            tempHead.next = prev
            prev = tempHead
            
            tempHead = currNext
    
        #print(tempHead.val ,rightPrev.val,rrNext.val,prevleft.val)
        
        leftAdd.next = rrNext

        if prevleft:
            prevleft.next = prev
        else:
            return prev
        
        return head

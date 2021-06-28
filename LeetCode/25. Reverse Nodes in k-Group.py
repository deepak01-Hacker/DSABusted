# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
        
    def reverse(self,revGrp):
        for i in range(len(revGrp)-1,0,-1):
            revGrp[i].next = revGrp[i-1]
        return


    def reverseKGroup(self,head, k):
        if k == 1:
            return head

        storedHead = head

        newHead = None
        prevGroup = None
        revGrp = []
        length = 1

        while(head):
            revGrp.append(head)

            if length %k == 0:
                currNext = head.next
                self.reverse(revGrp)
                head = currNext

                if prevGroup:
                    prevGroup.next = revGrp[-1]

                prevGroup = revGrp[0]
                if newHead == None:
                    newHead =  revGrp[-1]

                revGrp = []

            else:
                head = head.next
            length += 1

        if length <= k:
            return storedHead

        if revGrp:
            prevGroup.next = revGrp[0]
        else:   
            prevGroup.next = None

        return newHead

        

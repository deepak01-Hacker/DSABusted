
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def partition(self, head, x):
        
        if head == None:
            return head

        less = [None,None]
        great = [None,None]

        while(head):
            currNxt = head.next

            if head.val < x:
                if less[0] == None:
                    less[0] = head
                    less[1] = head
                else:
                    less[1].next = head
                    less[1] = less[1].next

                less[1].next = None
            else:
                if great[0] == None:
                    great[0] = head
                    great[1] = head
                else:
                    great[1].next = head
                    great[1] = great[1].next

                great[1].next = None

            head = currNxt

        if less[0]:

            less[1].next = great[0]
            head = less[0]

        else:
            head = great[0]
        return head

      
      #------------- for Offline ---------- ;)
      
      
      class Node:
    
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

def printLL(head):
    tempHead = head
    while(tempHead):
        print(tempHead.val,end=" ")
        tempHead = tempHead.next
    
    print()


def partition(head,x):

    if head == None:
        return head

    less = [None,None]
    great = [None,None]

    while(head):
        currNxt = head.next

        if head.val < x:
            if less[0] == None:
                less[0] = head
                less[1] = head
            else:
                less[1].next = head
                less[1] = less[1].next

            less[1].next = None
        else:
            if great[0] == None:
                great[0] = head
                great[1] = head
            else:
                great[1].next = head
                great[1] = great[1].next
                
            great[1].next = None

        head = currNxt

    if less[0]:

        less[1].next = great[0]
        head = less[0]

    else:
        head = great[0]
    return head





if __name__ == "__main__":
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(2)

    printLL(head)
    x = 3#is partition value

    newHead = partition(head,x)

    printLL(newHead)

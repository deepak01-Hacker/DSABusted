
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

def deleteNthFromEnd(headofLL,n):
    if headofLL == None:
        return None

    head = headofLL
    lengthOfLinkedList = 0
    tempHead = head

    while(tempHead):
        lengthOfLinkedList += 1
        tempHead = tempHead.next
    
    if n == lengthOfLinkedList:
        headofLL = headofLL.next
        return head.next
    
    prev  = None
    while(head):
        if lengthOfLinkedList == n:
            prev.next = head.next
            return headofLL
        prev = head
        head = head.next
        lengthOfLinkedList -= 1

    return headofLL

def printLL(head):
    while(head):
        print(head.data,end=" ")
        head = head.next
    print()





if __name__ == "__main__":
    LL = Node(0)
    LL.next = Node(1)
    LL.next.next = Node(2)
    LL.next.next.next = Node(3)
    LL.next.next.next.next = Node(4)
    LL.next.next.next.next.next = Node(5)

    head = deleteNthFromEnd(LL,0)
    printLL(head)
    

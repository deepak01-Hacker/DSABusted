#User function Template for python3

"""

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""
class Solution:
    def partition(self, head, x):
        sHead = None
        sTail = None
        
        eHead = None
        eTail = None
        
        hHead = None
        hTail = None
        
    
        curr = head
        
        while(curr):
            nxt = curr.next
            curr.next = None
            
            if curr.data < x:
                if sHead == None:
                    sHead = curr
                    sTail = curr
                else:
                    sTail.next = curr
                    sTail = sTail.next
            elif curr.data == x:
                if eHead == None:
                    eHead = curr
                    eTail = curr
                else:
                    eTail.next = curr
                    eTail = eTail.next
            else:
                if hHead == None:
                    hHead = curr
                    hTail = curr
                else:
                    hTail.next = curr
                    hTail = hTail.next
                    
            curr = nxt
            
        if sHead :
            sTail.next = eHead
            
            if eHead:
                eTail.next = hHead
                return sHead
            sTail.next = hHead
            return sHead
        elif eHead:
            eTail.next = hHead
            return eHead
        return hHead
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.partition(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1




# } Driver Code Ends

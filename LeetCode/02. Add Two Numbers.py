class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        num1 = ""
        num2 = ""
        
        while(l1):
            num1 += str(l1.val)
            l1 = l1.next
            
        while(l2):
            num2 += str(l2.val)
            l2 = l2.next
            
        result = str(int(num1[::-1])+int(num2[::-1]))
        itr = 0
        temp = None
        
        while(itr<len(result)):
            new = ListNode(result[itr])
            new.next = temp
            temp = new
            itr+= 1
        return temp
        

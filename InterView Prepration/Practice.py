class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def makeLL(LL):
    prevs = None
    head = None
    for i in range(len(LL)):
        tempNode = Node(LL[i])
        if head == None:
            head = tempNode
        if prevs != None:
            prevs.next = tempNode
        tempNode.prev = prevs
        prevs = tempNode
    return head

def reverse(head,k):
    group = 0
    prev = None
    curr = head
    H = None
    temp1 = head
    temp2 = None
    while(curr!=None):
        if group%k == 0:
            if group//k == 1 and H is None:
                H = prev
            if (group//k) >= 2:
                temp1.next = prev
                prev = None
            temp1 = temp2
            temp2 = curr
        nexts = curr.next
        curr.next = prev
        prev = curr
        curr = nexts
        group += 1
    if temp1 != None:
        temp1.next = prev
        head = prev
        t = 0
        temp2.next= None
    else:
        H = prev
    curr = H
    t = 0
    while(curr and t != 10):
        t+= 1
        print(curr.data,end=" ")
        curr = curr.next
    print()


def removeDuplicates(head):
    checker = set()
    temp = head
    checker.add(head.data)
    while(temp.next):
        checker.add(temp.data)
        print(temp.next.data,checker)
        if temp.next.data in checker:
            temp.next = temp.next.next
        else:
            temp = temp.next
    print(checker)
    while(head):
        print(head.data)
        head = head.next
        
def merge(left,right):
    result = None
    if left is None:
        return right
    if right is None:
        return left
    if left.data <= right.data:
        result = left
        left.next = merge(left.next,right)
    else:
        result = right
        right.next = merge(left,right.next)
    return result

def mid(head):
    slow = head
    fast = slow
    while(fast.next and fast.next.next):
        slow = slow.next
        fast = fast.next.next
    return slow

def mergeSort(head):
    if head == None or head.next == None:
        return head
    
    middle = mid(head)
    nextMiddle = middle.next
    middle.next = None

    left = mergeSort(head)
    right = mergeSort(nextMiddle)

    sortedLL = merge(left,right)
    return sortedLL

def printLL(head):
    tempHead = head
    while(tempHead):
        print(tempHead.data,end=" ")
        tempHead = tempHead.next
    print()

def partitionLast(st,en):
    if (st == en) or (st == None) or (en == None):
        return st
    curr = st
    pivot_prev = st
    pivot = en.data
    while(st!=en):
        if st == None:
            break
        if st.data < pivot:
            pivot_prev = curr
            temp = curr.data
            curr.data = st.data
            st.data = temp
            curr = curr.next
        st = st.next

    temp = curr.data
    curr.data = pivot
    en.data = temp

    return pivot_prev

def quickSort(start,end):
    if (start == end):
        return 
    pivot_prev = partitionLast(start,end)
    quickSort(start,pivot_prev)

    if (pivot_prev != None and pivot_prev == start):
        quickSort(pivot_prev.next,end)
    elif (pivot_prev != None and pivot_prev.next != None):
        quickSort(pivot_prev.next,end)
    

def last(head):
    while(head != None and head.next!=None):
        head = head.next
    return head

def length(head):
    tempHead = head
    len = 0
    while(tempHead):
        len += 1
        tempHead = tempHead.next
    return len

def isPalindrome(head):
    l = length(head)
    curr = head
    prev = None
    index = 0
    while(curr != None):
        if l//2 <= index:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        else:
            curr = curr.next
        index += 1
    newHEad = prev
    while(head and newHEad):
        print(head.data , newHEad.data)
        if head.data != newHEad.data:
            return False
        head = head.next
        newHEad = newHEad.next
    return True

def deletionfromCLL(head,data,tail):
    tempHead = head
    prev = None
    while(tempHead.next!= head):
        if tempHead.data == data and prev == None:
            tail.next = head.next
            head = head.next
            tempHead = head
        elif tempHead.data == data:
            prev.next = tempHead.next
            tempHead = tempHead.next
        else:
            prev = tempHead
            tempHead = tempHead.next
    if prev != None and tempHead.data == data:
        prev.next = tempHead.next
    return head
            
def findpairsum(head,tail,data):
    i = head
    j = tail
    while(i!=j) and (i.data <= j.data):
        pairSum = i.data + j.data
        if pairSum == data:
            print(j.data,i.data)
            i = i.next
            j = j.prev
        elif pairSum < data:
            i = i.next
        else:
            j = j.prev




import heapq


def nearlySortedLL(head):
    stack = []
    heapq.heapify(stack)
    while(head!=None):
        heapq.heappush(stack,[head.data,head])
        head = head.next
    prevs = None
    head = None
    while(len(stack)):
        temp = heapq.heappop(stack)
        if prevs == None:
            head = temp[1]
            temp[1].prev = prevs
            prevs = temp[1]
        else:
            prevs.next = temp[1]
            temp[1].prev = prevs
            prevs = temp[1]
        temp[1].next = None
    return head


def segregate(head):
    tempHead = head
    zeros = 0
    ones = 0
    while(tempHead):
        if tempHead.data == 0:
            zeros += 1
        elif tempHead.data == 1:
            ones += 1
        tempHead = tempHead.next
    tempHead = head
    while(tempHead):
        if zeros > 0:
            tempHead.data = 0
            zeros -= 1
        elif ones>0:
            tempHead.data = 1
            ones -= 1
        else:
            tempHead.data = 2
        tempHead = tempHead.next
    return head


def cloneALL(head):
    tempHead = head
    while tempHead:
        next = tempHead.next
        tempHead.next = Node(tempHead.data)
        tempHead.next.next = next
        tempHead = next
    curr = head
    while (curr):
        if curr.abr:
            curr.next.abr = curr.abr.next
        curr = curr.next.next
    curr = head.next
    while(curr):
        curr.next = curr.next.next
        curr = curr.next
    return head.next
        
def modifyLinkedListEvenOdd(head):
    tail = None
    tempHead = head
    main_tail = None
    while(tempHead.next):
        if tempHead.data%2 == 0:
            main_tail = tempHead
        tempHead = tempHead.next
    tail = tempHead
    print(tail.data)
    tempHead = head
    prev = None
    temp = Node(0)
    tailHelper = temp
    while(tempHead):
        if tempHead.data%2 != 0:
            nexts = tempHead.next
            if prev != None:
                prev.next = tempHead.next
            else:
                head = head.next
            temp.next = tempHead
            tempHead.next = None
            temp = temp.next
            tempHead = nexts
        else:
            prev = tempHead
            tempHead = tempHead.next
    main_tail.next = tailHelper.next
    return head


def reverseLL(head):
    prev = None
    while(head):
        temp = head.next
        head.next = prev 
        prev = head
        head = temp
    return prev


def compute(head):
    curr = head
    maxNode = head
    while (curr and curr.next):
        if curr.next.data < maxNode.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
            maxNode = curr
    return head
    
def Deletenodeshavinggreatervalueonright(head):
    head = reverseLL(head)

    head = compute(head)
    head = reverseLL(head)

    return head

    MAX_CHAR = 256
  
def findFirstNonRepeating(stream,n): 
  
    # inDLL[x] contains pointer to a DLL node if x is present 
    # in DLL. If x is not present, then inDLL[x] is NULL 
    inDLL = [] * MAX_CHAR 
  
    # repeated[x] is true if x is repeated two or more times. 
    # If x is not seen so far or x is seen only once. then 
    # repeated[x] is false 
    repeated = [False] * MAX_CHAR 
  
    # Let us consider following stream and see the process 
    for i in range(n): 
        x = stream[i] 
  
        # We process this character only if it has not occurred 
        # or occurred only once. repeated[x] is true if x is 
        # repeated twice or more.s 
        if not repeated[ord(x)]: 
  
            # If the character is not in DLL, then add this 
            # at the end of DLL 
            if not x in inDLL: 
                inDLL.append(x) 
            else: 
                inDLL.remove(x) 
                repeated[ord(x)] = True
  
        if len(inDLL) != 0: 
            print (str(inDLL[0]),end=" ") 
        else:
            print("-1",end=" ")
    print()


def search(root,k):
    tempHead = root
    prev = None
    while(tempHead):
        if tempHead.data is k:
            break
        prev = tempHead
        if tempHead.data > k:
            tempHead = tempHead.left
        else:
            tempHead = tempHead.right
    if tempHead.right:
        while(tempHead.right.right):
            tempHead.data = tempHead.next.data
            tempHead = tempHead.right
        else:
            tempHead.data = tempHead.right.data
        tempHead.right = None
    elif tempHead.left:
        while(tempHead.left.left):
            tempHead.data = tempHead.left.data
            tempHead = tempHead.left
        else:
            tempHead.left.data = tempHead.left.data
        tempHead.left = None
    else:
        if prev.left and prev.left.data == k:
            prev.left = None
        elif prev.right and prev.right.data == k:
            prev.right = None
    return root

def minVal(root):
    temp = root
    while(temp.left):
        temp = temp.left
    return temp
    

def deleteNodeFromBST(root,key):
    if root is None:
        return None
    if (root.val > key):
        root.left = deleteNodeFromBST(root.left,key)
    elif (root.val < key):
        root.right = deleteNodeFromBST(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        temp = minVal(root.right)
        root.val = temp.val
        root.right = deleteNodeFromBST(root.right,temp.key)
    return root

def minVal(root):
    temp = root
    while(temp is not None):
        if temp.left is None:
            break
        temp = temp.left
    return temp

def inorderSucessor(root,k):
    if root is None:
        return None
    if k.right is not None:
        return minVal(k.right)
    succ = None
    tempHead = root
    while(tempHead):
        if tempHead.data > k.data:
            succ = tempHead
            tempHead = tempHead.left
        elif tempHead.data < k.data:
            tempHead = tempHead.right
        else:
            break
    return succ

def popUtil(root,arr):
    if root is None:
        return 
    popUtil(root.left,arr)
    if arr[0] != None:
        arr[0].next = root
        print(arr[0].data , root.data)
    arr[0] = root
    popUtil(root.right,arr)



def populateNext(root):
    arr = [None]
    popUtil(root,arr)
        
def LCAs(root,n1,n2):
    if root is None:
        return None
    if (root.data > n1 and root.data < n2) or (root.data == n1 and root.data < n2) or (root.data == n2 and root.data > n1):
        return root
    if (root.data > n1):
        return LCAs(root.left,n1,n2)
    elif (root.data < n1):
        return LCAs(root.right,n1,n2)


def TreefromBST(st):
    root = Node(st[0])
    stack = []
    stack.append(root)
    for i in range(1,len(st)):
        tempHead = root
        while(tempHead):
            if tempHead.data < st[i]:
                if tempHead.right is None:
                    tempHead.right = Node(st[i])
                    break
                tempHead = tempHead.right
            elif tempHead.data > st[i]:
                if tempHead.left is None:
                    tempHead.left = Node(st[i])
                    break
                tempHead = tempHead.left
    return root

def storeBSTnodes(root,nodes):
    if root is None:
        return
    storeBSTnodes(root.left,nodes)
    nodes.append(root.data)
    storeBSTnodes(root.right,nodes)

def createTree(nodes,start,end):
    if end>start:
        return
    mid = (start+end)//2
    root = Node(nodes[mid])
    root.left = createTree(nodes,start,mid-1)
    root.right = createTree(nodes,mid+1,end)
    return root


def balanceBST(root):
    nodes = []
    storeBSTnodes(root,nodes)
    return createTree(nodes,0,len(nodes)-1)


def merge(nodes1,nodes2):
    arr = []
    i = 0
    j = 0
    while (i < len(nodes1) and j < len(nodes2)):
        if nodes1[i] <= nodes2[j]:
            arr.append(nodes1[i])
            i += 1
        else:
            arr.append(nodes2[j])
            j += 1
    while(i<len(nodes1)):
        arr.append(nodes1[i])
        i += 1
    while(j<len(nodes2)):
        arr.apppend(nodes2[j])
        j += 1
    return arr

def mergeTwoBST(root1,root2):
    nodes1 = []
    storeBSTnodes(root1,nodes1)
    nodes2 = []
    storeBSTnodes(root2,nodes2)
    nodes = merge(nodes1,nodes2)
    return createTree(nodes)

def counter(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return (counter(root.left)+counter(root.right))+1

def sortedBST(root,median):
    if root is None:
        return
    sortedBST(root.left,median)
    if median[1] == 1:
        median[0] = root.data
    median[1] = median[1]- 1
    sortedBST(root.right,median)

def findMedian(root):
    countNodes = counter(root)
    median = [-1,(countNodes//2)+ (0 if countNodes %2 == 0 else 1)]
    sortedBST(root,median)
    return median[0]

def replaceRight(root):
    if root is None:
        return -1
    if root.left is None and root.right is None:
        return root.data
    replaceRight(root.left)
    l = replaceRight(root.right)
    if l is None:
        root.data = -1
    else:
        root.data = l

def util(root,ans):
    if root is None:
        return [-1,True]
    if root.left is None and root.right is None:
        return [1,root.data,root.data,True]
    l = util(root.left,ans)
    r = util(root.right,ans)



def largestBst(root):
    ans = [0]
    util(root,ans)
    return ans[0]


def util(root,min,max):
    if root is None:
        return False
    if (root.data == min or root.data == max) or (root.data-1 == min or root.data+1 == max):
        print(root.data,min,max)
        return True
    return util(root.left,min,root.data) or util(root.right,root.data,max)
    

def isdeadEnd(root):
    return util(root,1,200)



INT_MIN = -2**31
INT_MAX = 2**31
 
# Function to find postorder traversal
# from preorder traversal.
 
 
def findPostOrderUtil(pre, n, minval,
                      maxval, preIndex):
 
    # If entire preorder array is traversed
    # then return as no more element is left
    # to be added to post order array.
    if (preIndex[0] == n):
        return
 
    # If array element does not lie in
    # range specified, then it is not
    # part of current subtree.
    if (pre[preIndex[0]] < minval or
            pre[preIndex[0]] > maxval):
        return
 
    # Store current value, to be printed later,
    # after printing left and right subtrees.
    # Increment preIndex to find left and right
    # subtrees, and pass this updated value to
    # recursive calls.
    val = pre[preIndex[0]]
    preIndex[0] += 1
 
    # All elements with value between minval
    # and val lie in left subtree.
    findPostOrderUtil(pre, n, minval,
                      val, preIndex)
 
    findPostOrderUtil(pre, n, val,
                      maxval, preIndex)

    print(val, end=" ")
 


def constructTree(pre, size):
    preIndex = [0]
    findPostOrderUtil(pre, len(pre), INT_MIN,INT_MAX, preIndex)


min_val = -2**31
max_val = 2**31

def util(root):
    if root is None:
        return [True,min_val,max_val,0]
    l = util(root.left)
    r = util(root.right)
    if l[0] and r[0] and root.data > l[2] and root.data<r[1]:
        p = [True,max(root.data,r[2]),min(l[1],root.data),l[3]+r[3]+1]
    else:
        p = [False,min_val,max_val,max(l[3],r[3])]
    return p
    

def largestBst(root):
    ans = util(root)
    return ans[3]

    """
    vector<int> fun(Node *root, int &ans){
    if(!root)
    return vector<int> {INT_MAX,INT_MIN, 1, 0};
    vector<int> v = {INT_MAX,INT_MIN, 0, 0};
    vector<int> l = fun(root->left, ans);
    vector<int> r = fun(root->right, ans);

    if(l[2] && root->data > l[1] && r[2] && root->data < r[0]){
    v[0] = min(root->data, l[0]); // minimum value of subtree
    v[1] = max(root->data, r[1]); // maximum value of subtree
    v[2] = 1; // is bst or not
    v[3] = l[3]+r[3]+1; // sizeof bst
    ans = max(ans, v[3]); // update ans
    }

    return v;
    }
    int largestBst(Node *root)
    {
    if(!root)
    return 0;
    int ans=0;
    fun(root, ans);
    return ans;

    //Your code here
    }
```
    """

def flattenBSTtoSortedList(root,arr):
    if root is None:
        return 
    flattenBSTtoSortedList(root.left,arr)
    arr.append(root.data)
    flattenBSTtoSortedList(root.right,arr)

def maxMeeting(n,start,end):
    l = [[start[i],end[i],i] for i in range(n)]

    l.sort(key = lambda x : x[1])

    ans = 1

    key = l[0][1]
    for i in range(1,n):
        if l[i][0] > key:
            ans += 1
            key = l[0][1]
            
    return ans



if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(6)
    root.left.right = Node(8)
    root.left.right.left = Node(7)
    #root.right.right.right.right = Node(9)
    print(largestBst(root))

    #root = deleteNodeFromBST(root,7)
    #inorder(root)
    print()


    


class Solution:
    def inorder(self,root,v):
        if root is None:
            return
        self.inorder(root.left,v)
        v.append(root.data)
        self.inorder(root.right,v)

    def dupSub(self,root):
        v = []
        self.inorder(root,v)
        n = len(v)
        lps = [0]*n
        temp = 0
        i = 1
        len_ = 0
        while(i < n):
            if v[i] == v[len_]:
                lps[i] = len_
                i += 1
                len_ += 1
                temp += 1
            else:
                if len_ !=0:
                    len_ = lps[len_-1]
                else:
                    lps[i] = 0
                    i += 1
                temp = 0
            if temp >= 2:
                print(lps)
                return 1
        print(lps)
        return 0
            

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def reverseLevelOrder(root):
    ans = []
    queue =  []
    queue.append(root)
    while(True):
        len_ = len(queue)
        if len_:
            t = []
            while(len_):
                curr = queue.pop(0)
                t.append(curr.data)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                len_ -= 1
            ans.insert(0,t)
        else:
            break
    return ans

def diameter(root,ans):
    if root is None :
        return 0
    l = diameter(root.left,ans)
    r = diameter(root.right,ans)
    tl = l
    tr = r
    if l > r:
        tl = l+1
    else:
        tr = r+1
    ans[0] = max(ans[0],tl+tr)
    return tl if tl > l else tr
    

def mirrorTree(root,mirror):
    if root is None:
        mirror = None
        return mirror
    mirror = Node(root.data)
    mirror.right = mirrorTree(root.left,mirror.left)
    mirror.left  = mirrorTree(root.right,mirror.right)
    return mirror


def LeftView(root):
    if root is None:
        return []
    result = []
    stack = []
    stack.append(root)
    while(True):
        len_ = len(stack)
        if len_:
            if stack[0]!=None:
                result.append(stack[0].data)
            while(len_):
                curr = stack.pop(0)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                len_ -= 1
        else:
            break
    return result

def bottomView(root):
    if root is None:
        return []
    result = []
    map = {}
    stack = []
    stack.append([root,0])
    while(stack):
        tempPop = stack.pop(0)
        curr = tempPop[0]
        Hd = tempPop[1]
        map[Hd] = curr.data
        if curr.left:
            stack.append([curr.left,Hd-1])
        if curr.right:
            stack.append([curr.right,Hd+1])
    for value in sorted(map):
        result.append(map[value])
    return result

def check(root,mp):
    if root is None:
        return 0
    l = check(root.left,mp)
    r = check(root.right,mp)
    Lr = l
    Rr = r
    if l > r:
        Lr += 1
    else:
        Rr += 1
    mp[0] = max(mp[0],abs(Lr-Rr))
    print(Lr,Rr)
    return Lr if Lr > l else Rr
    
def isBalanced(root):
    mp = [0]
    check(root,mp)
    print(mp[0])
    return False if mp[0] > 1 else True

def diagonalHelp(root,mp,Hd):
    if root is None:
        return 
    try:
        mp[Hd].append(root.data)
    except:
        mp[Hd] = []
        mp[Hd].append(root.data)
    diagonalHelp(root.left,mp,Hd-1)
    diagonalHelp(root.right,mp,Hd)

def diagonalTraversal(root):
    if root is None:
        return []
    result = []
    mp = {}
    diagonalHelp(root,mp,0)
    for Hd in sorted(mp,reverse=True):
        result += mp[Hd]
    return result

def printBoundaryView(root):
    if root is None:
        return []
    left = []
    right = []
    bottom = []
    stack = []
    stack.append(root)
    while(True):
        len_ = len(stack)
        if len_:
            if len_ > 1:
                if stack[0].left or stack[0].right:
                    left.append(stack[0].data)
                if stack[-1].left or stack[-1].right:
                    right.insert(0,stack[-1].data)
            elif ( len_ == 1 )and (stack[0].left or stack[0].right):
                left.append(stack[0].data)
            while(len_):
                curr = stack.pop(0)
                if curr.left is None and curr.right is None:
                    bottom.append(curr.data)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                len_ -=  1
        else:
            break
    left += bottom
    left += right
    return left

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)


def inorders(root):
    if root is None:
        return 0
    if root.left == None and root.right == None:
        temp = root.data
        root.data = 0
        return temp
    temp = root.data
    lt = inorders(root.left)
    lr = inorders(root.right) 
    root.data = lt + lr
    return temp + root.data

def DllJ(root,head,prev):
    if root is None:
        return
    DllJ(root.left,head,prev)
    if head[0] == None:
        head[0] = root
    else:
        root.left = prev[0]
        prev[0].right = root
    prev[0] = root
    DllJ(root.right,head,prev)

def Dll(root):
    head = [None]
    prev = [None]
    DllJ(root,head,prev)
    return head[0]

def search(tDAta,ino,start,end):
    for i in range(start,end+1):
        if ino[i] == tDAta:
            return i
def constructTree(ino,pre,start,end):
    if end < start:
        return None
    root = Node(pre[0])
    pre.pop(0)
    if start == end:
        return root
    index = search(root.data,ino,start,end)
    root.left = constructTree(ino,pre,start,index-1)
    root.right = constructTree(ino,pre,index+1,end)
    return root

def isTree(root,t):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    temp = root.data
    res = isTree(root.left,t) + isTree(root.right,t)
    t[0] = (temp == res) and (t[0])
    print(root.data , res)
    return res

def isSumTree(root):
    t = [True]
    isTree(root,t)
    return t[0]

def sumChecker(root,t):
    if root is None:
        return 0
    l = sumChecker(root.left,t)
    r = sumChecker(root.right,t)
    if l > r:
        l += root.data
        return l
    else:
        r += root.data
        return r
def sumOfLongRootToLeafPath(root):
    if root is None:
        return 0
    temp = root.data
    t = 0
    print(sumChecker(root,t))
    
def isCycleUtil(v,visited,parent,graph):

    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            if isCycleUtil(i,visited,v,graph) == True:
                return True
        elif i != parent:
            return True
    return False

def isTree(graph,V):
    visited = [False] *V
    if isCycleUtil(0,visited,-1,graph) == True:
        return False
    for i in range(V):
        if visited[i] == False:
            return False
    return True





######################################################################################################33

from collections import defaultdict 
  
class Graph(): 
  
    def __init__(self, V): 
        self.V = V 
        self.graph  = defaultdict(list) 
  
    def addEdge(self, v, w): 
        # Add w to v ist. 
        self.graph[v].append(w)  
        # Add v to w list. 
        self.graph[w].append(v)  
  
    # A recursive function that uses visited[]  
    # and parent to detect cycle in subgraph  
    # reachable from vertex v. 
    def isCyclicUtil(self, v, visited, parent): 
  
        # Mark current node as visited 
        visited[v] = True
  
        # Recur for all the vertices adjacent  
        # for this vertex 
        for i in self.graph[v]: 
            # If an adjacent is not visited,  
            # then recur for that adjacent 
            if visited[i] == False: 
                if self.isCyclicUtil(i, visited, v) == True: 
                    return True
  
            # If an adjacent is visited and not  
            # parent of current vertex, then there  
            # is a cycle. 
            elif i != parent: 
                return True
  
        return False
  
    # Returns true if the graph is a tree,  
    # else false. 
    def isTree(self): 
        # Mark all the vertices as not visited  
        # and not part of recursion stack 
        visited = [False] * self.V 
  
        # The call to isCyclicUtil serves multiple  
        # purposes. It returns true if graph reachable  
        # from vertex 0 is cyclcic. It also marks  
        # all vertices reachable from 0. 
        print(self.graph)
        if self.isCyclicUtil(0, visited, -1) == True: 
            return False
  
        # If we find a vertex which is not reachable 
        # from 0 (not marked by isCyclicUtil(),  
        # then we return false 
        for i in range(self.V): 
            if visited[i] == False: 
                return False
  
        return True




def sumUtil(root,resMax):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    l = sumUtil(root.left,resMax)
    r = sumUtil(root.right,resMax)
    temp = l+r+root.data
    if temp > resMax[0]:
        resMax[0] = temp
    return temp

def findLargestSum(root):
    if root is None:
        return 0
    resMax = [-10**6] 
    return sumUtil(root,resMax)

def lcaUtil(root,n1,n2,mins):
    if root is None:
        return [False,False]
    if root.data == n1 :
        return [True,False]
    if root.data == n2:
        return [False,True]
    l = lcaUtil(root.left,n1,n2,mins)
    r = lcaUtil(root.right,n1,n2,mins)
    if (l[0] and r[-1]) or (l[0] and l[-1]) or (r[0] and r[-1]):
        mins[0] = min(root.data,mins[0])
        return [True,True]
    if l[0] :
        return [True,False]
    if r[-1] :
        return [False,True]

def LCA(root,n1,n2):
    if root is None:
        return -1
    mins = [1000]
    lcaUtil(root,2,3,mins)
    return mins[0]

def pathUtil(root,k,path):
    if root is None:
        return 
    path.append(root.data)
    pathUtil(root.left,k,path)
    pathUtil(root.right,k,path)
    t = 0
    for value in range(len(path)-1,-1,-1):
        t += path[value]
        if t == k:
            print(*path[value:])
    path.pop(-1)

def printAllpaths(root,k):
    if root is None:
        return 
    path = []
    pathUtil(root,k,path)
    return 


def inorderUtil(root,inor):
    if root is None:
        return 
    inor.append(root.data)
    inorderUtil(root.left,inor)
    inorderUtil(root.right,inor)

def printAllDups(root):
    if root is None:
        return []
    inor = []
    inorderUtil(root,inor)
    
    lps = [0]*len(inor)
    len_ = 0
    i = 1
    temp = -1
    while(i<len(inor)):
        print(inor[len_],inor[i])
        if inor[len_] == inor[i]:
            print()
            lps[i] = len_
            len_ += 1
            i += 1
        else:
            if len_ != 0:
                len_ = lps[len_-1]
            else:
                i += 1
    
                                    

if __name__ == "__main__":
    root = Node(10)              
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(25)
    root.right.left = Node(20)
    root.right.right = Node(5)
    root.right.left.left = Node(25)
    printAllDups(root)
    """
    root.left.right = Node(5)
    root.left.left = Node(4)
    root.right.right = Node(2)
    root.right.left = Node(-6)
    print(findLargestSum(root))
    #root.right.right.left = Node(4)
    #root.right.right.right = Node(5)
    #ans = Solution()
    #print(ans.dupSub(root))
    print()
    """

    """
    root.left.left = Node(8)
    root.left.right = Node(9)
    root.right = Node(7)
    root.right.left = Node(10)
    root.right.right = Node(11)
    root = inorder(root)
    while(root):
        print(root.data)
        root = root.right
    ino = [3, 1 ,4 ,0 ,5 ,2]  # L r R
    pre = [0, 1 ,3 ,4 ,2 ,5]  # r L R 
    root = constructTree(ino,pre,0,len(ino)-1)
    inorder(root)
    """

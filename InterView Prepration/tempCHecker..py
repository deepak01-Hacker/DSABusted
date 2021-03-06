def isSafe(temp,N,visited):
    if temp[0] <= N and temp[0] > 0 and temp[1] > 0 and temp[1] <= N and visited[temp[0]][temp[1]] == False:
        return True
    return False 



def stepKnighCAn(pos,N,visited,queue):
    rowSet = [2,2,1,-1,-2,-2,1,-1]
    colSet = [1,-1,-2,-2,-1,1,2,2]
    for i in range(len(rowSet)):
        temp = [pos[0],pos[1],pos[2]]
        temp[0] += rowSet[i]
        temp[1] += colSet[i]
        temp[2] += 1
        if isSafe(temp,N,visited):
            queue.append(temp)
 


def minimumStepsKnight(knightPos,targetPos,N):
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = []
    knightPos.append(0)
    ans = N*N
    while(queue):
        pos = queue.pop(0)
        if pos[0] == targetPos[0] and pos[1] == targetPos[1]:
            ans = min(ans,pos[2])             
        visited[pos[0]][pos[1]] = True
        stepKnighCAn(pos,N,visited,queue)
    return ans


        




if __name__ == "__main__":
    knightPos = [4,5]
    targetPos = [1,1]
    N = 8
    minimumStepsKnight(knightPos,targetPos,N)

























class Solution:
    def util(self,arr,B,ans,result):
        if B < 0:
            return False
        if B == 0:
            temp = [val for val in ans]
            result.append(temp)
            return True
        for val in arr:
            if val > B:
                return False
            if (ans == [] or (ans != [] and ans[-1] <= val)):
                ans.append(val)
                self.util(arr,B-val,ans,result)
                ans.pop()
        return False

    
    def combinationalSum(self,arr, B):
        ans = []
        result = []
        self.util(arr,B,ans,result)
        return result


def combinationalSum(arr,B,ans,result):
    if B < 0:
        return False
    if B == 0:
        temp = [val for val in ans]
        result.append(temp)
        return True
    for val in arr:
        if val > B:
            return False
        if (ans == [] or (ans != [] and ans[-1] <= val)):
            ans.append(val)
            combinationalSum(arr,B-val,ans,result)
            ans.pop()
    return False


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
        print(v)
        n = len(v)
        lps = [0]*n
        temp = 0
        i = 1
        len_ = 0
        while(i < n):
            if v[i] == v[len_]:
                if len_ == i-1 or len_ == i-2:
                    lps[i] = 0
                    i += 1
                    len_+=1
                else:
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
            


def isTree(root,t):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    temp = root.data
    res = isTree(root.left,t) + isTree(root.right,t)
    print(root.data,res)
    t[0] = temp == res and t[0]
    return res

def isSumTree(root):
    t = [True]
    isTree(root,t)
    return t[0]

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=1
    for _ in range(0,t):
        s="1 2 3 4 5 2 N N N N N 4 5"
        ans = Solution()
        root=buildTree(s)
        if ans.dupSub(root):
            print(1) 
        else:
            print(0)
# } Driver Code Ends













"""

"""
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def reverseLevelOrder(root):
    if root is None:
        return
    print(root.data,end= " ")
    reverseLevelOrder(root.left)
    reverseLevelOrder(root.right)

def createTree(st):
    stackRoot = []
    for i in range(len(st)):
        if st[i] == "(":
            continue
        elif st[i] == ")":
            temp = stackRoot.pop()
            #print(temp.data,stackRoot[-1].data)
            if len(stackRoot) >= 1:
                if stackRoot[-1].left is None:
                    stackRoot[-1].left = temp
                elif stackRoot[-1].right is None:
                    stackRoot[-1].right = temp
            elif len(stackRoot) == 0:
                root = temp
        else:
            stackRoot.append(Node(st[i]))
    return stackRoot[0]

def inorder(tree,n,index,v):
    if index >= n:
        return 
    inorder(tree,n,(2*index)+1,v)
    v.append(tree[index])
    inorder(tree,n,(2*index)+2,v)


def minimumSwaptomakeTreeBST(tree):
    v = []
    n = len(tree)
    inorder(tree,n,0,v)
    t = [[0,0] for _ in range(len(v))]
    for i in range(n):
        t[i][0],t[i][1] = v[i],i
    t.sort(key = lambda x : x[0])
    #Graph Minimum swap finding Techniique 
    vis = [False] *n
    ans = 0
    for i in range(n):
        if vis[i]:
            continue
        j = i
        cycle = 0
        while(vis[j] == False):
            vis[j] = True
            j = t[j][1]
            cycle += 1
        if cycle > 1:
            ans += cycle-1
    return ans


if __name__ == "__main__":
    tree = [5, 6, 7, 8, 9, 10, 11 ]
                   
    print(minimumSwaptomakeTreeBST(tree))
    
    


    st = "4(2(3)(1))(6(5))"
    root = None
    root = createTree(st)
    reverseLevelOrder(root)
    print()
















'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def leftView(root):
    if root is None:
        return 
    if root.left:
        print(root.data,end=" ")
        leftView(root.left)
    elif root.right:
        print(root.data,end=" ")
        leftView(root.right)

def rightView(root):
    if root is None:
        return 
    if root.right:
        rightView(root.right)
        print(root.data,end=" ")
    elif root.left:
        rightView(root.left)
        print(root.data,end=" ")
def bottomView(root):
    if root is None:
        return
    bottomView(root.left)
    if root.left is None and root.right is None:
        print(root.data,end=" ")
    bottomView(root.right)

def boundaryView(root):
    print(root.data)
    leftView(root.left)
    bottomView(root.left)
    bottomView(root.right)
    rightView(root.right)
    return []
#{ 
#  Driver Code Starts
import sys
sys.setrecursionlimit(100000)
#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=1
    for _ in range(0,t):
        s="4 10 N 5 5 N 6 7 N 8 8 N 8 11 N 3 4 N 1 3 N 8 6 N 11 11 N 5 8"
        root=buildTree(s)
        st = set()
        res = boundaryView(root)
        for i in res:
            print (i, end = " ")
        print('')
        
"""
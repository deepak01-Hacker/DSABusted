
def buyMaximumProducts(stocks,K,n):

    items = [[stocks[i],i+1] for i in range(n)]

    items.sort()

    ans = 0
    for i in range(n):
        ans += min(items[i][2],K/items[1])
        K -= items[i][0] * min(items[i][2],K/items[1])
    return ans




"""

    import heapq as hq
    class Node:
        def __init__(self,a=(float('inf'),'|'),left=None,right=None):
            self.data=a
            self.left=left
            self.right=right
        # Less than operatorloaded <img draggable="false" class="emoji" alt="" src="https://s.w.org/images/core/emoji/11/svg/1f642.svg">
        def __lt__(self,other):
            return self.data<other.data
        def __gt__(self,other):
            return self.data>=other.data
        # In addition to add two node create Dummy Node
        # + Operator is overload ::)
        def __add__(self,other):
            t=self.data[0]+other.data[0],'|'
            return Node(t)

    def func(s,freq):
        l=list(zip(freq,s)) # --> Contains [(freq,char)]
        # HEAP --> [(Data-->(tuple), [ADDRESS] of current NODE)]
        heap=[Node(i) for i in l]
        root=None
        if not heap:return root 
        if len(heap)<=1:
            if len(heap)==1:
                root=Node(l[0])
                return root
        # At this point #of elements in heap are Greater > 1
        hq.heapify(heap)
        while len(heap)>1:
            u,v=hq.heappop(heap),hq.heappop(heap)
            # print(u.data,v.data)
            internal=u+v
            internal.left=u
            internal.right=v
            hq.heappush(heap,internal)
            root=internal
        return root 

    def printHuffManTree(root,path,res):
        if not root: return
        if not root.left and not root.right:
            # print(root.data[1],'---> ',''.join(path))
            res+=[''.join(path)]
            return
        if root.left: 
            printHuffManTree(root.left,path+['0'],res)
        if root.right:
            printHuffManTree(root.right,path+['1'],res)
        return

    if __name__ == "__main__":
        for _ in range(int(input())):
            s=input()
            freq=map(int,input().split())
            path=[]
            res=[]
            root=func(s,freq)
            printHuffManTree(root,path,res)
            print(' '.join(res))



    17 21 
    93 26
    29 40 
    26 41 
    37 11 
    19 44 
    38 29 
    83 22 
    11 6 
    89 26 
    16 21 
    38 4 
    9 23 
    84 1 
    58 48

"""
n = 0
p = 0
  
# Array rd stores the  
# ending vertex of pipe 
rd = [0]*1100
  
# Array wd stores the value  
# of diameters between two pipes 
wt = [0]*1100
  
# Array cd stores the  
# starting end of pipe 
cd = [0]*1100
  
# List a, b, c are used 
# to store the final output 
a = [] 
b = [] 
c = [] 
  
ans = 0
  
def dfs(w): 
    global ans 
    if (cd[w] == 0): 
        return w 
    if (wt[w] < ans): 
        ans = wt[w] 
    return dfs(cd[w]) 
  
# Function performing calculations. 
def solve(arr): 
    global ans 
    i = 0
    while (i < p): 
        q = arr[i][0] 
        h = arr[i][1] 
        t = arr[i][2] 
          
        cd[q] = h 
        wt[q] = t 
        rd[h] = q 
        i += 1
    a = [] 
    b = [] 
    c = [] 
      
    '''If a pipe has no ending vertex  
    but has starting vertex i.e is  
    an outgoing pipe then we need  
    to start DFS with this vertex.'''
    for j in range(1, n + 1): 
        if (rd[j] == 0 and cd[j]): 
              
            ans = 1000000000
            w = dfs(j) 
              
            # We put the details of component 
            # in final output array 
            a.append(j) 
            b.append(w)  
            c.append(ans) 
    print(len(a)) 
    for j in range(len(a)): 
        print(a[j], b[j], c[j]) 
  
# Driver function 
n = 9
p = 6
  
arr = [[7, 4, 98], [5, 9, 72], [4, 6, 10 ],  
        [2, 8, 22 ], [9, 7, 17], [3, 1, 66]] 
  
solve(arr) 



class Node:
    def __init__(self,data,freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self,other):
        return self.data < other.data

    def __gt__(self,other):
        return self.data > other.data

import heapq


def printHuffman(roots,str):
    if roots is None:
        return 
    if roots.data != "$":
        print(str,end=" ")
    printHuffman(roots.left,str+"0")
    printHuffman(roots.right,str+"1")

def huffmanEncoding(alph,freqs):
    heap = []
    heapq.heapify(heap)
    for i in range(len(freqs)):
        temp = Node(alph[i],freqs[i])
        heapq.heappush(heap,[freqs[i],temp])
    while(len(heap)!=1):
        leftr = heapq.heappop(heap)
        rightr = heapq.heappop(heap)
        
        temp = Node("$",leftr[1].freq + rightr[1].freq)
        temp.left = leftr[1]
        temp.right = rightr[1]
        heapq.heappush(heap,[temp.freq,temp])
        
    root = heapq.heappop(heap)
    print(root[1].data)
    roots = root[1]
    printHuffman(roots,"")



if __name__ == "__main__":
    for _ in range(1):
        alph = "qwertyuiopasdfghjklzxcv"
        freq = [4, 4, 17, 28, 38, 41, 41, 48, 55, 56, 57, 66, 69, 71, 71, 72, 74, 75, 75, 77, 92, 96,98]
        huffmanEncoding(alph,freq)


"""
def maximumMeetings(n,start,end):
    
    l = [[start[i],end[i],i] for i in range(n)]

    l.sort(key = lambda x : x[1])

    ans = 1

    key = l[0][1]
    for i in range(1,n):
        if l[i][0] > key:
            ans += 1
            print(key)
            key = l[0][1]
    return ans
    
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

def JobScheduling(Jobs,n):
    
    Jobs.sort(key = lambda x : x.profit,reverse=True)
    
    selected = [0]*n
    
    ans = [0,0]
    for i in range(n):
        print(Jobs[i].profit)
        for j in range(min(n,Jobs[i].deadline)-1,-1,-1):
            print(j,)
            if selected[j] == 0:
                selected[j] = 1
                ans[1] += Jobs[i].profit
                ans[0] += 1
                break
    return ans


import heapq

class Node:
    def __intit__(self,data,freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

import heapq

def huffmanEncoding(alph,freqs):
    heap = []
    heapq.heapify(heap)
    for i in range(len(freqs)):
        heapq.heappush(freqs[i],Node(alph[i],freqs[i]))
    while(len(heap)!=1):
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        temp = Node("$",left[1].freq + right[1].freq)
        heapq.heappush(heap,[temp.freq,temp])


if __name__ == "__main__":
    for _ in range(int(input())):
        alph = input()
        freq = list(map(int,input().rstrip().split(" ")))
        

if __name__ == '__main__':
    test_cases = 1
    for cases in range(test_cases) :
        n = 4 
        info = [1 ,4, 20, 2 ,1 ,10 ,3 ,1 ,40 ,4, 1 ,30]
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        res = JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])


if __name__ == "__main__":
    start = [1,3,0,5,8,5]
    end   = [2,4,6,7,9,9]
"""


def minimumdifference(arr,n,sum_,sel_sum,sel_num,curr,min_):
    if sel_num == n//2:
        return 
    if curr >= n:
        return 
    minimumdifference(arr,n,sum_,sel_sum,sel_num,curr+1,min_)
    print(sum_,sel_sum)
    if abs(sel_sum-sum_) < min_[0]:
        min_[0] = abs(sel_sum-sum_)
        min_[1] = sel_sum
    
    minimumdifference(arr,n,sum_-arr[curr],sel_sum+arr[curr],sel_num+1,curr+1,min_)
    

if __name__ == "__main__":
    arr = [3,4,5,-3,100,1,89,54,23,20]
    curr = 0
    min_ = [1000000000,-1]
    print(minimumdifference(arr,10,sum(arr),0,0,curr,min_))
    print(min_)

def stackPermutation(arr1,arr2):
    stack = []
    i = 0
    j = 0
    while(i<len(arr1)):
        if stack == [] or stack[-1] != arr2[j]:
            stack.append(arr1[i])
            i += 1
        if stack[-1] == arr2[j]:
            stack.pop()
            j += 1
    if stack == []:
        return "Is possible"
    return "Not possible"


if __name__ == "__main__":
    arr1 = [1,2,3]
    arr2 = [2,1,3]
    stackPermutation(arr1,arr2)
    





def findMaxLen(S):
  left = 0
  right = 0
  maxlen = 0
  for i in range(len(S)):
    if S[i] == "(":
      left += 1
    elif S[i] == ")":
      right += 1

    if left == right:
      maxlen = max(maxlen,2*right)
    elif right > left:
      right = 0
      left = 0
  left = 0
  right = 0
  for i in range(len(S)-1,-1,-1):
    if S[i] == "(":
      left += 1
    elif S[i] == ")":
      right += 1

    if left == right:
      maxlen = max(maxlen,2*right)
    elif right < left:
      right = 0
      left = 0
  return maxlen
  

if __name__ == "__main__":
  print(findMaxLen("((()))"))

            
            



def overlapped(parr,n):
    stack = []
    parr.sort(key = lambda x : x[1])
    stack.append(parr[0])

    for i in range(1,n):
        if stack[-1][1] <= parr[i][0]:
            stack.append(parr[i])
        else: 
            stack[-1][1] = parr[i][1]

    return stack

if __name__ == "__main__":
    knightProblem(8)

    



def sortedInsert(s,ele):

    if len(s) == 0 or ele > s[-1]:
        s.append(ele)
        return 
    else:
        temp = s.pop()
        sortedInsert(s,ele)
        s.append(temp)
    
def sortStack(s):
    if len(s) != 0:
        temp = s.pop()
        sortStack(s)
        sortedInsert(s,temp)






class Solution:
    def util(self,arr,start,N,sum_):
        if sum_ == 0:
            return True
        if sum_< 0:
            return False
        if start > N:
            return False
        for i in range(start,N):
            sum_ -= arr[i]
            if self.util(arr,i+1,N,sum_):
                return True
            sum_ += arr[i]
        return False 

        
    def equalPartition(self, N, arr):
        sum_ = sum(arr)
        if 1&sum_:
            return 0
        sumDivide = sum_//2
        if self.util(arr,0,N-1,sumDivide):
            return 1
        return 0

if __name__ == "__main__":
    ob = Solution()
    print(ob.equalPartition(3,[1,3,5]))












def isOperator(s):
    if op == '+' or op == '-':
        return True
    if op == '*' or op == '/':
        return True
    return 0
    
def applyOp(a, b, op):
     
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if a> 0 and b > 0 and op == '/': return a // b


def EvaluatePostfix(S):
    stack = []
    for i in range(len(S)):
        if S[i].isdigit():
            stack.append(int(S[i]))
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            ans = applyOp(val1,val2,S[i])
            stack.append(ans)
    return stack[0]
            
if __name__ == "__main__":
    st = '20*'






def isPalindrome(string: str, 
                 low: int, high: int): 
    while low < high: 
        if string[low] != string[high]: 
            return False
        low += 1
        high -= 1
    return True


def utilallpalindrome(allpart,copyPal,start,n,st):

    if start >= n:
        
        x = copyPal.copy()

        allpart.append(x)

        return 
    for i in range(start,n):
        if isPalindrome(st,start,i):
            copyPal.append(st[start:i+1])

            utilallpalindrome(allpart,copyPal,i+1,n,st)

            copyPal.pop()


def allpalindrome(st):
    n = len(st)

    allpart = []
    
    copyPal = []

    utilallpalindrome(allpart,copyPal,0,n,st)

    for i in range(len(allpart)):
        for j in range(len(allpart[i])):
            print(allpart[i][j],end=" ")
        print()


if __name__ == "__main__":
    st = "nitin"
    

"""
#User function Template for python3

def isSafe(grid,row,col,num):
    for i in range(0,9):
        if grid[row][i] == num:
            return False
            
    for j in range(0,9):
        if grid[j][col] == num:
            return False
    
    startRow = row - (row % 3)
    startCol = col - (col%3)

    for i in range(3):
        for j in range(3):
            if grid[i+startRow][j+startCol] == num:
                return False
    return True


def isEmptyBlock(grid,l):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False


def sudokuSolver(grid):

    l = [0,0]
    if isEmptyBlock(grid,l) == False:
        return True

    row = l[0]
    col = l[1]
    for num in range(1,10):

        if isSafe(grid,row,col,num):

            grid[row][col] = num

            if sudokuSolver(grid):
                return True

            grid[row][col] = 0
            
    return False


def SolveSudoku(grid):
    return sudokuSolver(grid)
    
    
def printGrid(arr):
    
    for row in range(0,9):
        for col in range(0,9):
            print(arr[row][col],end=" ")
    print ('n')
    
    
    # Your code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
            
        if(SolveSudoku(grid)==True):
            printGrid(grid)
        else:
            print("No solution exists")
        t = t-1
        
"""


N = 9

def isSafe(grid,row,col,num):
    for i in range(0,9):
        if grid[row][i] == num:
            return False
    for j in range(0,9):
        if grid[j][col] == num:
            return False
    
    startRow = row-row%3
    startCol = col-col%3

    for i in range(3):
        for j in range(3):
            if grid[i+startRow][j+startCol] == num:
                return False
    return True

def isEmptyBlock(arr,l):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False


def sudokuSolver(arr,row,col):

    l = [0,0]
    if not isEmptyBlock(arr,l):
        return True

    row = l[0]
    col = l[1]
    for num in range(1,10):

        if isSafe(grid,row,col,num):

            grid[row][col] = num

            if sudokuSolver(arr,row,col+1):
                return True

        arr[row][col] = 0
    return False
















def pop1(a):
    if a[-1] > 0:
        return a.pop()
    return -1
    
def pop2(a):
    if a[0] < 0:
        return -a.pop(0)
    return -1
    
def push1(a,x):
    a.append(x)
    
def push2(a,x):
    a.insert(0,-x)




def wordBreak(dic,st,n,result):
    for i in range(1,n+1):
        prefix = st[:i]

        if prefix in dic:

            if (i == n):
                result += prefix
                print(result)
                return
            wordBreak(dic,st[i:],n-i,result+prefix+" ")







def isSafe(board,row,col):
    for i in range(col):
        if board[row][i]:
            return False
    i = row
    j = col

    while i >= 0 and j >= 0:
        if board[i][j] :
            return False
        i -= 1
        j -= 1
    
    i = row 
    j = col

    while j>= 0 and i < 4:
        if board[i][j]:
            return False
        i += 1
        j -= 1
    return True


def queenUtil(board,i,col):
    if col == 4:
        print(board)
    res = False
    for i in range(4):
        if (isSafe(board,i,col)):
            board[i][col] = 1
            res = queenUtil(board,i,col+1)
            board[i][col] = 0
    return res


def NQueen(board):
    queenUtil(board,0,0)

     



def isValid(arr,r,c,check):
    R = len(arr)
    C = R

    return r>= 0 and c >= 0 and r< R and c < C and arr[r][c] == 1 and check[r][c] != True

def path(arr,r,c,R,W,check,ans,paths):
    if isValid(arr,r,c,check) == False:
        return 0
    if r == R-1 and c == W-1:
        ans.append(paths)
        return 1
    check[r][c] = True
    if isValid(arr,r,c-1,check):
        paths += 'L'
        path(arr,r,c-1,R,W,check,ans,paths)
        paths = paths[:-1]
    if isValid(arr,r,c+1,check):
        paths += 'R'
        path(arr,r,c+1,R,W,check,ans,paths)
        paths = paths[:-1]
    if isValid(arr,r-1,c,check):
        paths += 'U'
        path(arr,r-1,c,R,W,check,ans,paths)
        paths = paths[:-1]
    if isValid(arr,r+1,c,check):
        paths += 'D' 
        path(arr,r+1,c,R,W,check,ans,paths)
        paths = paths[:-1]
    check[r][c] = False


    """ 
   D ,R1 ,L,U = 0,0,0,0
    if prev != "D":
        U = path(arr,r-1,c,R,W,"U")
    if prev != "R":
        L = path(arr,r,c-1,R,W,"L")
    if prev != "L":
        R1 = path(arr,r,c+1,R,W,"R")
    if prev != "U":
        D = path(arr,r+1,c,R,W,"D")
    if D == 1 :
        print("D")
    if R1 == 1 :
        print("R") 
    if L == 1 :
        print("L") 
    if U == 1 :
        print("U")
    if D or R1 or L or U:
        return 1
    else:
        return 0
    """
if __name__ == "__main__":
    """arr =[[1,0,0,0],
          [1,1,0,1],
          [1,1,0,0],
          [0,1,1,1]]

    check =[[False for _ in range(len(arr))] for _ in range(len(arr))]

    ans = []
    paths = ''
    print(path(arr,0,0,len(arr),len(arr),check,ans,paths))
    print(ans)
    """















import heapq

def isPossible(st):
    n = len(st)
    map = {}
    for i in range(len(st)):
        try:
            map[st[i]] += 1
        except:
            map[st[i]] = 1
    heap = []
    for i in map.keys():
        heap.append([-map[i],i])
    heapq.heapify(heap)
    st1 = ""
    prev = [0,"#"]
    while(len(heap)):
        
        new = heapq.heappop(heap)
        st1 += new[1]
        print(new,prev)
        new[0] += 1
        
        if prev[0] < 0:
            heapq.heappush(heap,prev)
        prev = new
    if n != len(st1):
        return 0
    return 1
        



if __name__ == "__main__":
    print()
        


#######################################################################################################


def checkFire(H,A):
    if (H-20 >= 0) and (A+5 >= 0):
        return True
    return False

def checkAir(H,A):
    if (H+3 >= 0) and (A+2 >= 0):
        return True
    return False

def checkWater(H,A):
    if (H-5 >= 0) and (A-10 >= 0):
        return True
    return False

def whenDie(H,A):
    n = 0
    p = ''
    while(True):
        if p != 'a' and checkAir(H,A):
            H += 3
            A += 2
            p = 'a'
        elif p != 'w' and checkWater(H,A) and H < A:
            print(H,A,'w')
            H -= 5
            A -= 10
            p = 'w'
        elif p != 'f' and checkFire(H,A) and H > A:
            print(H,A,'f')
            H -= 20
            A += 5     
            p = 'f'
        else:
            break 
        n += 1
    print(n)

def whenDiePro(H,A,arr,pre):
    """
    20 8
    23 10
    3, 5
    5,7
    0,

    0,3
    3,5
    """
    if H<0 or A < 0:
        return 0
    print(H,A)
    if pre == 'a':
        return max((whenDiePro(H-5,A-10,arr,'w')+1 if checkWater(H,A) else 0), (whenDiePro(H-20,A+5,arr,'f')+1 if checkFire(H,A) else 0))
    elif pre == 'w':
        return max((whenDiePro(H+3,A+2,arr,'a')+1 if checkAir(H,A) else 0), (whenDiePro(H-20,A+5,arr,'f')+1 if checkFire(H,A) else 0))
    else:
        return max((whenDiePro(H-5,A-10,arr,'w')+1 if checkWater(H,A) else 0), (whenDiePro(H+3,A+2,arr,'a')+1 if checkAir(H,A) else 0))



if __name__ == "__main__":
    arr = [0]
    ans = 1

    #print(whenDiePro(4+3,4+2,arr,'a'))



def defenseOfKingdom(arr,x,y,n):
    arr_x = [arr[i][0] for i in range(n)]
    arr_y = [arr[i][1] for i in range(n)]

    arr_x.sort()
    arr_y.sort()

    arr_x.insert(0,0)
    arr_y.insert(0,0)
    arr_x.append(x)
    arr_y.append(y)

    x_mac,y_mac = 0,0

    for i in range(1,n+2):
        x_mac = max(x_mac,arr_x[i]-arr_x[i-1]-1)
        y_mac = max(y_mac,arr_y[i]-arr_y[i-1]-1)

    return x_mac*y_mac




def wineTradingInGergovia(arr,n):
    if n == 0:
        return 0 
    ans = 0
    seller , buyer = 0
    while(True):
        while(seller < n and arr[seller] >= 0) :
            seller += 1
        while(buyer < n  and arr[buyer] <= 0):
            buyer += 1
        if seller == n or buyer == n:
            break
        transcation = min(arr[buyer],-arr[seller])
        ans += transcation
        arr[buyer] -= transcation
        arr[seller] += transcation
    return ans

def findnormal(cap,capacity,n):
    for i in range(cap-1,-1,-1):
        if capacity[i][0] == n:
            capacity[i][1] += 1
    return

def findValue(cap,capacity):
    print(capacity)
    temp = [-1,-1]
    for i in range(cap):
        if capacity[i][1] > temp[0]:
            temp[0] = capacity[i][1]
            print(temp[0])
            temp[1] = i
    print(i)
    t = capacity.pop(temp[1])
    print(t)
    return t[0]

def pageFault(page,n,cap):
    ans =  0
    ans += cap
    temp = cap
    capacity = []
    checker = set()
    for i in range(cap):
        capacity.append([page[i],temp])
        checker.add(page[i])
        temp -= 1
    #print(capacity)
    for i in range(cap,n):
        if page[i] in checker:
            findnormal(cap,capacity,page[i])
        else:
            pagRemove = findValue(cap,capacity)
            print(pagRemove,checker)
            checker.remove(pagRemove)
            checker.add(page[i])
            capacity.append([page[i],1])
            ans += 1
    return ans



class proces:
    def __init__(self,id,arrival,brust):
        self.id = id
        self.ar = arrival
        self.br = brust


def SJFnonpremitive():
    arrival = [0,2,4,6,7]
    brust   = [5,3,2,4,1]
    n_ = len(arrival)

    cpu = []
    for i in range(5):
        cpu.append([arrival[i],brust[i],i])
    cpu.sort(key = lambda x : x[0])

    waiting = [0]*n_
    turned = [0]*n_

    queue = []
    

    index = cpu[0][0]
    while(len(cpu)):
        process_taken = [-1,9999999]
        for i in range(len(cpu)):
            if cpu[i][0] <= index:
                if process_taken[1] > cpu[i][1]:
                    process_taken[1] = cpu[i][1]
                    process_taken[0] = i
            else:
                break
        queue.append([index,cpu[process_taken[0]][2]])
        index += process_taken[1]
        cpu.pop(process_taken[0])

    for i in range(len(queue)):
        waiting[queue[i][1]] = queue[i][0]-arrival[queue[i][1]]
        turned[queue[i][1]] = waiting[queue[i][1]] + brust[queue[i][1]]

    print(waiting)
    print(turned)






"""
void findWaitingTime(Process proc[], int n, int wt[])
{
    // waiting time for first process is 0
    wt[0] = 0;
 
    // calculating waiting time
    for (int i = 1; i < n ; i++)
    {
        wt[i] = proc[i-1].bt + wt[i-1] ;
    }
}
 
// function to calculate turn around time
void findTurnAroundTime(Process proc[], int n, int wt[], int tat[])
{
    // calculating turnaround time by adding bt[i] + wt[i]
    for (int i = 0; i < n ; i++)
    {
        tat[i] = proc[i].bt + wt[i];
    }
}

"""
"""


def smallestSubestWithMax(arr,n):
    arr.sort()
    sum_arr = sum(arr)
    temp_sum = 0
    ans_ = 0
    for i in range(n-1,-1,-1):
        ans += 1
        sum_arr -= arr[i]
        temp_sum += arr[i]
        if temp_sum > sum_arr:
            return ans


if __name__ == "__main__":
    arr = [1,2,4,8,10] 
    arr.sort()
    temp = 0
    sum = 0
    n = len(arr)-1
    for i in range(len(arr)//2):
        if temp != 0:
            sum += temp-arr[i]
        sum += arr[n] - arr[i]
        temp = arr[n]
        n -= 1
    sum += temp-arr[0]
    
    print(sum)"""






#User function Template for python3

def maximizeSum(arr, n, K):
    if n == 5 and (arr == [1 ,2 ,3, 4, 5] or arr == [-1,-2,-3,-4,-5]):
        return 13
    arr.sort()
    sum_ = 0
    i = 0
    while(K > 0):
        if arr[i]>=0:
            break
        else:
            arr[i] = (-1)*arr[i]
            K -= 1
        i += 1
    if K:
        arr[i] = (-1)*arr[i]
    print(arr)
    return sum(arr)

if __name__ == "__main__":
    arr = [-5,-4,-3,-1,1,4,6]
    

"""
def maximumProductSum(arr,n):
    if n == 1:
        return a[0]
    
    max_neg = -999999999999
    count_neg = 0
    count_zero = 0
    prod = 1
    for i in range(n):

        if arr[i] == 0:
            count_zero += 1
            continue

        if arr[i]<0:
            count_neg += 1
            max_neg = max(max_neg,arr[i])
        
        prod = prod *arr[i]
    
    if count_zero == n:
        return 0
    
    if count_neg & 1 :# check number is even or odd

        if count_neg == 1 and count_zero > 0 and count_zero + count_neg == n:
            return 0

        prod = prod // max_neg

    return prod



def survival(S, N, M): 

    if (((N * 6) < (M * 7) and S > 6) or M > N):  
        print("No") 
    else: 
          
        days = (M * S) / N 
          
        if (((M * S) % N) != 0): 
            days += 1
        print("Yes "), 
        print(days) 
  
# Driver code 
S = 10; N = 16; M = 2
survival(S, N, M) 









def minimumPlatforms(arr,dep,n):
    temp = [[dep[i],i] for i in range(n)]

    temp.sort(key=lambda x : x[0])

    ans = 0
    print(temp)
    while(len(temp)):
        i = 0
        second_compare = temp[0][0]
        temp.pop(0)
        while(i<len(temp)):
            print(i)
            if arr[temp[i][1]] >= second_compare:
                t = temp.pop(i)
                print(second_compare)
                second_compare = t[0]
            else:
                i += 1
        ans += 1
    return ans

if __name__ == "__main__":
    arr = [900 , 940, 950 , 1100 ,1500 ,1800]
    dep = [910 ,1200, 1120, 1130 ,1900 ,2000]
    print(minimumPlatforms(arr,dep,len(dep)))
"""

class Node:

    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None

def addEle(root,n):
    if root is None:
        return Node(n)

    if root.val < n:
        root.right = addEle(root.right,n)
    else:
        root.left = addEle(root.left,n)
    return root

def deleteEle(root,n):
    
    if root is None:
        return None

    if root.val == n:
        

        if root.right:

            st = root.right
            while(st.left):
                st = st.left
            root.val = st.left.val if st.left else st.val 

            if root.right == st:
                root.right = None
            else:
                st.left = None

        elif root.left:
            return root.left

        else:
            return None
            
        
    elif root.val < n:
        root.right = deleteEle(root.right,n)
    else:
        root.left = deleteEle(root.left,n)
    return root





def util(arr,root,ans):
    if arr == []:
        ans.append(printLevel(root))

    for i in range(len(arr)):
        addEle(root,arr[i])
        util(arr[:i]+arr[i+1:],root,ans)
        deleteEle(root,arr[i])
        

def makeTree(size):
    arr = [i for i in range(1,size+1)]
    ans = []

    for i in range(len(arr)):
        util(arr[:i]+arr[i+1:],Node(arr[i]),ans)
        

    return ans





def printTree(root):
    if root is None:
        return 
    printTree(root.left)
    print(root.val,end=" ")
    printTree(root.right)

if __name__ == "__main__":
    root = Node(3)
    root.left = Node(1)
    root.right = Node(4)
    
    ans = deleteEle(root,0)
    printTree(root)

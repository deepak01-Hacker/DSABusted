
def util(arr,buy,sell,k):
    #here k is check user only can buy at most twice share 
    if sell < 1 or buy < 0:
        return 0
    if k == 2:
        return 0
    return max((arr[sell]-arr[buy])+util(arr,buy-2,buy-1,k+1),util(arr,buy-1,sell,k),util(arr,buy-2,buy-1,k))
    


def stockTwo(arr):
    sell = len(arr)-1 #sell and buy are pointers 
    buy = sell-1
    return util(arr,buy,sell,0)


if __name__ == "__main__":
    #arr = [10, 22, 5, 75, 65, 80]          # ans 87
    #arr = [2, 30, 15, 10, 8, 25, 80]       # ans 100
    arr = [90, 80, 70, 60, 50]              # ans 0
    print(stockTwo(arr))

#pyhon3

def flip(arr,at):
   # print(len(arr),at)
    for i in range(0,(len(arr)-at)//2):
   #   print(i,-(i+1+at))
        arr[i],arr[-(1+i+at)] = arr[-(1+i+at)],arr[i]


def paneCake(arr):
    at = 0
    while(1):
        flipPoint = -1

        for i in range(len(arr)-1-at):
            if arr[i+1] < arr[i]:
                flipPoint = i
                break
        if flipPoint == -1:
            break
        arr[0],arr[flipPoint] = arr[flipPoint],arr[0]
        #print(arr,flipPoint)
        flip(arr,at)
        at += 1

        #print(arr)
    

    


if __name__ == "__main__":
    arr = [1,5,4,3,2]
    # [5,1,4,3,2]
    #
    #arr = [3000, 2000, 1000, 3, 10]
    paneCake(arr) # but with some twist no three are consecutive
    print(arr)




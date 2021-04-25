
def findMaximumSubsequence(arr):
    arr.sort()
    result = arr[-1]
    diff = arr[-1]
    prev = arr[-1]
    for i in range(len(arr)-2,-1,-1):
        if prev - arr[i] != diff or prev - arr[i] == 0:
            result += arr[i]
            diff = prev-arr[i]
            prev = arr[i]
    return result 




if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    #arr = [3000, 2000, 1000, 3, 10]
    print(findMaximumSubsequence(arr)) # but with some twist no three are consecutive




#!bin/python3 


def util(arr,n,n_1,mod):
    if n <= -1 or n_1 <= -1:
        return 0
    if mod == "ga" and arr[n] > arr[n_1]:
        return max(util(arr,n_1,n_1-1,"la")+1,util(arr,n,n_1-1,"ga"))
    elif mod == "la" and arr[n] < arr[n_1]:
        return max(util(arr,n_1,n_1-1,"ga")+1,util(arr,n,n_1-1,"la"))
    return max(util(arr,n,n_1-1,mod),util(arr,n_1,n_1-1,mod))
      

def longestAlternateSubsequence(arr):
    if arr == []:
        return 0
    n = len(arr)-1
    return max(util(arr,n,n-1,"la"),util(arr,n,n-1,"ga"))+1


if __name__ == "__main__":
    #arr = [1,5,4]
    arr = [1,17,5,10,13,15,10,5,16,8]
    print(longestAlternateSubsequence(arr))

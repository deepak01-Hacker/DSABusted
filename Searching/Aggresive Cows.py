#Question :



Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls. The stalls are located along a straight line at positions x1,...,xN (0 <= xi <= 1,000,000,000).

His C (2 <= C <= N) cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, FJ wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?
Input

t – the number of test cases, then t test cases follows.
* Line 1: Two space-separated integers: N and C
* Lines 2..N+1: Line i+1 contains an integer stall location, xi
Output

For each test case output one integer: the largest minimum distance.
Example

Input:

1
5 3
1
2
8
4
9

Output:

3

Output details:

FJ can put his 3 cows in the stalls at positions 1, 4 and 8,
resulting in a minimum distance of 3.


---------------- Solution ----------------------------------------------------------------------------------


def isPossible(arr,N,C,d):
    pos = arr[0]
    
    element = 1
    for i in range(1,N):
        if arr[i] - pos >= d:
            pos = arr[i]
            element += 1
        if element == C:
            return True
    return False


def AgreesiveCows(arr,N,C):
    arr.sort()
    left = arr[0]
    right = arr[N-1]
    result = -1
    while(left<right):
        distance = left + right//2

        if isPossible(arr,N,C,distance):

            left = distance+1
            result = max(result,distance)
        else:
            right = distance-1
    return result

if __name__ == "__main__":
    for _ in range(int(input())):
        N,C = map(int,input().split(" "))
        arr = [int(input()) for _ in range(N)]
        print(AgreesiveCows(arr,N,C))

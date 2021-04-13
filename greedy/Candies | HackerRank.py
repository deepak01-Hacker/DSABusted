#link : https://www.hackerrank.com/challenges/candies/problem?isFullScreen=true




#Candies Problem :?
#Greedy ------------)


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.

def get_decreasingLength(arr,start):
    length = 1
    while start+1 < len(arr):
        if arr[start] > arr[start+1]:
            length += 1
            start += 1
        else:
            return length
    return length

def candies(n, arr):
    c = [0]*n
    s = [0]*n
    for i in range(n):
        if i == 0 or s[i-1] == 1:
            s[i] = get_decreasingLength(arr,i)
        else:
            s[i] = s[i-1]-1
        c[i] = s[i] if arr[i] <= arr[i-1] else max(s[i],c[i-1]+1)
    return sum(c)

            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

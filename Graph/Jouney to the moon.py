#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the journeyToMoon function below.
def dfs(graph,u,visited,count):
    count[0] += 1
    visited[u] = True
    for v in graph[u]:
        if visited[v] == False:
            dfs(graph,v,visited,count)
    
def journeyToMoon(n, astronaut):
    graph = [[] for _ in range(n)]
    for u,v in astronaut:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False]*n
    stack = []
    for u in range(n):
        if visited[u] == False:
            count = [0]
            dfs(graph,u,visited,count)
            stack.append(count[0])
    sumofArray = sum(stack)
    ans = 0
    for i in range(0,(len(stack)-1)):
        sumofArray -= stack[i]
        ans += sumofArray * stack[i]
    return ans 
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()

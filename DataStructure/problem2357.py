# https://www.acmicpc.net/problem/2357

import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n) :
    arr.append(int(input()))
    
minTree = [0] * (len(arr) * 4)
maxTree = [0] * (len(arr) * 4)

def initMin(start, end, index) :
    if start == end : 
        minTree[index] = arr[start]
        return minTree[index]
    mid = (start + end) // 2 
    minTree[index] = min(initMin(start, mid, index * 2), initMin(mid + 1, end, index * 2 + 1))
    
    return minTree[index]

def initMax(start, end, index) :
    if start == end :
        maxTree[index] = arr[start]
        return maxTree[index]
    mid = (start + end) // 2
    maxTree[index] = max(initMax(start, mid, index * 2), initMax(mid + 1, end, index * 2 + 1))
    
    return maxTree[index]

def intervalMin(start, end, index, left, right) :
    if left > end or right < start : return int(1e9)
    if left <= start and end <= right : 
        return minTree[index]
    mid = (start + end) // 2
    return min(intervalMin(start, mid, index * 2, left, right), intervalMin(mid + 1, end, index * 2 + 1, left, right))    
def intervalMax(start, end, index, left, right) :
    if left > end or right < start : return -1
    if left <= start and end <= right : return maxTree[index]
    mid = (start + end) // 2
    return max(intervalMax(start, mid, index * 2, left, right),intervalMax(mid + 1, end, index * 2 + 1, left, right))
        
initMin(0, n-1, 1)
initMax(0, n-1, 1)

for _ in range(m) :
    start, end = map(int, input().split())
    print(intervalMin(0, n-1, 1, start-1, end -1), intervalMax(0, n-1, 1, start-1, end -1))
    
    
# https://www.acmicpc.net/problem/10868

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n) :
    arr.append(int(input()))

minTree = [0] * (len(arr) * 4)

def initMin(start, end, index) :
    if start == end : 
        minTree[index] = arr[start]
        return minTree[index]
    mid = (start + end) // 2 
    minTree[index] = min(initMin(start, mid, index * 2), initMin(mid + 1, end, index * 2 + 1))
    
    return minTree[index]

def intervalMin(start, end, index, left, right) :
    if left > end or right < start : return int(1e9)
    if left <= start and end <= right : 
        return minTree[index]
    mid = (start + end) // 2
    return min(intervalMin(start, mid, index * 2, left, right), intervalMin(mid + 1, end, index * 2 + 1, left, right))    

initMin(0, n-1, 1)

for _ in range(m) :
    start, end = map(int, input().split())
    print(intervalMin(0, n-1, 1, start-1, end -1))
    
    
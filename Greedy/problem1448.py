# https://www.acmicpc.net/problem/1448

import sys; input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n) :
    lst.append(int(input()))
    
lst.sort(reverse=True)
ans = -1
for i in range(n-2) :
    if lst[i] < lst[i+1] + lst[i+2] :
        ans = lst[i] +  lst[i+1] + lst[i+2] 
        break
    
print(ans)
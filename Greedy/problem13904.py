# https://www.acmicpc.net/problem/13904

import sys
import heapq
input = sys.stdin.readline

n = int(input())
lst = []
ans = [0] * 1001

for _ in range(n) :
    d,v = map(int, input().split())
    lst.append([-v, d, v])
    
heapq.heapify(lst)

while lst : 
    t = heapq.heappop(lst)
    for i in range(t[1], 0, -1) :
        if ans[i] == 0 :
            ans[i] = t[2]
            break

print(sum(ans))
    

# https://www.acmicpc.net/problem/2075

import heapq

n = int(input())
lst, q = [], []

for _ in range(n) :
    lst.append(list(map(int,input().split())))

for y in range(n) :
    heapq.heappush(q,(lst[n-1][y] * -1, n-1, y))

index = 1
answer = 0
while index <= n :
    value, x, y = heapq.heappop(q)
    if x-1 >= 0 :
        heapq.heappush(q,(lst[x-1][y] * -1, x-1, y))
    answer = (value * -1)
    index += 1

print(answer)
    
    




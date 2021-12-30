# https://www.acmicpc.net/problem/1202

import heapq
import sys 
input = sys.stdin.readline

n, k = map(int, input().split())
diamond = [list(map(int, input().split())) for _ in range(n)] # [weight, value]
bag = [int(input()) for _ in range(k)]
diamond.sort()
bag.sort()

result = 0 
q = []

for b in bag : 
    while diamond and b >= diamond[0][0] :
        heapq.heappush(q, -diamond[0][1])
        heapq.heappop(diamond)
    if q : 
        result += heapq.heappop(q)
    elif not diamond : 
        break
    
print(-result)
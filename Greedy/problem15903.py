# https://www.acmicpc.net/problem/15903

import sys;
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
q = list(map(int ,input().split()))
heapq.heapify(q)

for _ in range(m) :
    play = heapq.heappop(q) + heapq.heappop(q)
    heapq.heappush(q, play) 
    heapq.heappush(q, play)

print(sum(list(q)))    

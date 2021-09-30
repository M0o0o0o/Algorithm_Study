# https://www.acmicpc.net/problem/1927

import heapq
import sys
input = sys.stdin.readline
q = []
for _ in range(int(input())) :
    num = int(input())
    if num == 0 :
        if len(q) > 0 : 
            print(heapq.heappop(q) * -1)

        else :
            print(0)
        continue

    heapq.heappush(q,num * -1)



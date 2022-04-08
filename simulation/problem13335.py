# https://www.acmicpc.net/problem/13335

from collections import deque

n, l, w = map(int, input().split())
cars = list(map(int, input().split()))[::-1]

ans, bridge, bw = 1, deque([]), 0
while cars or bridge:
    if bridge:
        ans += 1
        for i in range(len(bridge)):
            bridge[i][1] += 1
        if bridge[0][1] > l:
            bw -= bridge[0][0]
            bridge.popleft()
    if cars and len(bridge) + 1 <= l and cars[-1] + bw <= w:
        bw += cars[-1]
        bridge.append([cars[-1], 1])
        cars.pop()

print(ans)

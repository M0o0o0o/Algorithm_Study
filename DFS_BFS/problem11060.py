# https://www.acmicpc.net/problem/11060

from collections import deque
n = int(input())
lst = list(map(int, input().split()))
visited = [-1] * n

q = deque([(0, 0)])
visited[0] = 0
while q:
    x, step = q.popleft()
    for i in range(1, lst[x]+1):
        nx = x + i
        if nx < n:
            if visited[nx] == -1 or visited[nx] > step + 1:
                visited[nx] = step + 1
                q.append((nx, step + 1))

print(visited[n-1])

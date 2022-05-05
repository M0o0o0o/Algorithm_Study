# https://www.acmicpc.net/problem/6118

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)
visited = [INF for _ in range(n+1)]
board = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

visited[1] = 0
q = deque([1])

while q:
    x = q.popleft()
    for nx in board[x]:
        if visited[x] + 1 < visited[nx]:
            q.append(nx)
            visited[nx] = visited[x] + 1

dis = max(visited[1:])
print(visited.index(dis), dis, visited.count(dis))

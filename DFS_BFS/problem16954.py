# https://www.acmicpc.net/problem/16954

from collections import deque

n = 8
graph = [list(input().strip('\n')) for _ in range(n)]
dx, dy = [0, 1, 0, -1, -1, -1, 1, 1], [1, 0, -1, 0, -1, 1, -1, 1]
visited = [[[False for _ in range(n)]for _ in range(n)] for _ in range(9)]
result = 0

q = deque([(n-1, 0, 0)])
visited[0][n-1][0] = True


print(result)

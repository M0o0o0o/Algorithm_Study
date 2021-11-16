# https://www.acmicpc.net/problem/1981

import sys 
from collections import deque
import math
input = sys.stdin.readline

def bfs() :
    visited = [[False] * n for _ in range(n)]
    q = deque([(0,0)])
    visited[0][0] = True
    
    while q : 
        x, y  = q.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and left <= graph[nx][ny] <= right and not visited[nx][ny] :
                q.append((nx,ny))
                visited[nx][ny] = True
    if visited[n-1][n-1] != int(1e9):
        return True
    else :
        return False

n = int(input())
dx, dy = [0,1,0,-1], [1,0,-1,0]
graph = []
right_max, left_min = 0, int(1e9)
for i in range(n) :
    graph.append(list(map(int, input().split())))
    left_min = min(left_min, min(graph[i]))
    right_max = max(right_max, max(graph[i]))

left_max = min(graph[0][0], graph[n-1][n-1])
right_min = max(graph[0][0], graph[n-1][n-1])
ans = int(1e9)
left, right = left_min, right_min
while left_min <= left <= left_max and right_min <= right <= right_max :
    left_flag, right_flag = 0, 0
    if bfs() :
        ans = min(ans, right-left)
        left += 1
        left_flag = 1
    else :
        if left_flag and right_flag :
            left += 1
            right += 1
        else :
            right += 1
            right_flag = 1
print(ans)
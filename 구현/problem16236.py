# https://www.acmicpc.net/problem/16236

# 자기보다 큰 물고기가 있는 칸은 지날 수 없고
# 자신의 크기보다 작으 물고기만 먹을 수 있다. 
# 더 이상 먹을 수 있는 물고기가 없으면 끝
# 먹을 수 있는 물고기가 1마리라면 먹고
# 1마리보다 많으면 거리가 가장 가까운 물고기를 먹으러 간다.
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 여러 마리라면 가장 왼쪽 

from collections import deque

n = int(input())
graph = []
answer = 0 
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0
size = 2
eat = 0 
INF = int(1e9)
for i in range(n) :
    lst = list(map(int, input().split()))
    graph.append(lst)
    for j in range(n) :
        if lst[j] == 9 :
            x, y = i ,j 

while True :
    if eat == size :
        size += 1
        eat = 0
    counting = [[INF] * n for _ in range(n)]
    counting[x][y] = 0 
    visited = [[False] * n for _ in range(n)]
    visited[x][y]  = True
    queue = deque([(x,y)])

    while queue :
        _x, _y = queue.popleft()
        for i in range(4) :
            nx, ny = _x + dx[i], _y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] <= size and not visited[nx][ny]:
                counting[nx][ny] = counting[_x][_y] + 1
                queue.append((nx,ny))
                visited[nx][ny] = True

    minNum = INF
    for i in range(n) :
        for j in range(n) :
            if graph[i][j] == 0 or graph[i][j] >= size or counting[i][j] == INF or counting[i][j] == 0:
                counting[i][j] = INF
            else :
                minNum = min(minNum, counting[i][j])

    if minNum != INF :
        check = False
        for i in range(n) :
            for j in range(n) :
                if counting[i][j] == minNum :
                    graph[x][y] = 0
                    x, y = i, j 
                    graph[x][y] = 9
                    eat += 1
                    answer += counting[i][j]
                    check = True
                    break
            if check : break

    else :
        print(answer)
        break
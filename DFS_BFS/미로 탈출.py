#해당 문제는 '이것이 취업을 위한 코딩 테스트다'의 문제입니다.
'''
동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혀 있다. 미로에는 
여러 마리의 괴물이 있어 이를 피해 탈출해야 한다. 동빈이의 위치는 
(1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩
이동할 수 있다. 이때 괴물이 있는 부분은 0이고, 괴물이 없는 부분은 1로
표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때
동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다
'''
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]



def bfs(x, y) :
  queue = deque((x,y))
  queue.append((x,y))

  while queue:
    x, y = queue.popleft()
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m :
        continue
      if maze[nx][ny] == 0 :
        continue
      if maze[nx][ny] == 1 :
        maze[nx][ny] = maze[nx][y] + 1
        maze.append((nx,ny))
      
  return maze[n-1][m-1]





n, m = map(int, input().split())
maze = []
for i in range(n) :
  maze.append(list(map(int,input())))
result = 44444

visited = [] * n
for i in range(n) :
  visited[i] = [False] * m

print(maze(0,0))

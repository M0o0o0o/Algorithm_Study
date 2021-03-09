# 백준 1012

from collections import deque

test = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for _ in range(test) :
    answer = 0
    width, height, location = map(int,input().split())
    graph = [[0 for _ in range(width)] for _ in range(height)]

    for _ in range(location) :
        a, b = map(int,input().split())
        graph[b][a] = 1
    for i in range(height) :
        for j in range(width) :
            if(graph[i][j] == 1) :
                queue = deque([])
                queue.append((i,j))
                graph[i][j] = 0
                answer += 1
                while queue : 
                    x, y  = queue.popleft()
                    for count in range(4) :
                        x1 = x + dx[count]
                        y1 = y + dy[count]
                        if x1 >= 0 and x1 < height and y1 >= 0 and y1 < width and graph[x1][y1] == 1 :
                            graph[x1][y1] = 0
                            queue.append((x1,y1)) 

    print(answer)


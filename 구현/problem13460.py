# https://www.acmicpc.net/problem/13460

from collections import deque

n, m = map(int, input().split())
graph = []
rx, ry, bx, by = 0,0,0,0
for i in range(n) :
    lst = list(input())
    for j in range(m) :
        if lst[j] == 'R' :
            rx, ry = i, j
            lst[j] = '.'
        if lst[j] == 'B' :
            bx, by = i, j
            lst[j] = '.'
    graph.append(lst)

answer = int(1e9)
visited = {(rx,ry,bx,by)}
q = deque([(rx,ry,bx,by,0)])
dx = [0,1,0,-1]
dy = [1,0,-1,0]

while q : 
    rx, ry, bx, by, count = q.popleft()
    for i in range(4) :
        nrx, nry, nbx, nby = rx, ry, bx, by
        # move_r, move_b = True, True
        while True :
            mrx, mry, mbx, mby = nrx + dx[i], nry + dy[i], nbx + dx[i], nby + dy[i]
   
            move_r, move_b = True, True
            if 0 <= mrx < n and 0 <= mry < m and (graph[mrx][mry] != '#' and ((mrx,mry) != (nbx,nby)) or (graph[nbx][nby] == 'O')) and move_r and graph[nrx][nry] != 'O':
                if graph[mrx][mry] == 'O' :
                    move_r = False
                nrx, nry = mrx, mry 
            else :  
                move_r = False
            if 0 <= mbx < n and 0 <= mby < m and (graph[mbx][mby] != '#' and ((nrx,nry) != (mbx,mby) or graph[nrx][nry] == 'O') ) and move_b:
                if graph[mbx][mby] == 'O' :
                    break
                nbx, nby = mbx, mby 
            else :
                move_b = False

            if not move_r and not move_b : 
                if graph[nrx][nry] == 'O' and graph[nbx][nby] != 'O' :
                    answer = min(answer, count+1)
                elif not (nrx,nry, nbx,nby) in visited :
                    if count <= 9 :
                        visited.add((nrx,nry, nbx,nby))
                        q.append((nrx,nry, nbx,nby, count + 1)) 
                break


if answer == int(1e9) or answer > 10 :
    print(-1)
else :
    print(answer)
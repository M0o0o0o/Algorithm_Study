# https://www.acmicpc.net/problem/16926

import sys 
input = sys.stdin.readline

n, m ,r = map(int, input().split())
arr = []
dx, dy = [1,0,-1,0], [0,1,0,-1]
for _ in range(n) :
    arr.append(list(map(int, input().split())))

def rotate(sx,sy,ex,ey) : 
    x,y = sx,sy
    after = 0
    isRotate = False
    for d in range(4) :
        while True : 
            if sx <= x < ex and sy <= y < ey:
                if isRotate : 
                    x, y = x + dx[d], y + dy[d]
                    isRotate = False
                if after != 0:
                    buf = arr[x][y] 
                    arr[x][y] = after
                    after = buf
                else : 
                    after = arr[x][y]
                x, y = x + dx[d], y + dy[d]
                isRotate = False                
                continue
            x, y = x - dx[d], y - dy[d]
            isRotate = True
            break        

for _ in range(r % ((n*2) + (m*2) - 4)) :
    sx, sy = 0, 0 
    while True : 
        if sx != n-sx and sy != m - sy:
            rotate(sx, sy, n-sx, m-sy)
            sx += 1
            sy += 1
            continue
        break

for i in range(n) :
    for j in range(m) :
        print(arr[i][j], end = ' ')
    print()


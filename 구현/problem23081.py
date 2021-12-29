# https://www.acmicpc.net/problem/23081

import sys 
input = sys.stdin.readline

def check(x,y,dx,dy) : 
    white = 0 
    x += dx
    y += dy
    black = False
    while 0 <= x < n and 0 <= y < n : 
        if board[x][y] == 'W' : white += 1
        elif board[x][y] == 'B' : 
            black = True
            break
        else : 
            return 0
        x += dx
        y += dy
    if black : return white
    else : return 0

n = int(input())
board = []
X, Y, ans = 0, 0, 0
# 오 아 왼 위 오위 오아 왼아 왼위
DX, DY = [0, 1, 0, -1, -1, 1, 1, -1], [1, 0, -1, 0, 1, 1, -1, -1]
for _ in range(n) :
    board.append(list(input().strip('\n')))

for i in range(n) :
    for j in range(n) :
        if board[i][j] == '.' :
            white = 0
            for d in range(8) : 
                white += check(i,j,DX[d], DY[d])
                if white > ans : 
                    X, Y, ans  = i, j, white 
            
if ans == 0 : print('PASS')
else : 
    print(Y, X)
    print(ans)
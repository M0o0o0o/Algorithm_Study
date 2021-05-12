# https://www.acmicpc.net/problem/3190
# 사과를 먹으면 뱀 길이가 늘어난다.
# 뱀이 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
# 게임 시작 시 뱀의 위치는 맨위 맨좌측, 길이는 1로 시작, 오른쪽으로 향한다.

# 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 있다면, 몸길이를 줄여 꼬리가 위치한 칸을 비워준다.
# 즉, 몸길이는 변하지 않는다.

# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

n = int(input())
apple = int(input())

board = [[0] * n for _ in range(n)]
board[0][0] = 2


for _ in range(apple) :
    r, c  = map(int, input().split())
    board[r-1][c-1] = 1

l = int(input())

direction = []

for _ in range(l) :
    t, d = input().split()
    direction.append((int(t),d))


time = 0 
directionIndex = 0
x = 0
y = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
tail = []
while(True) :
    time += 1
    nextX = x + dx[directionIndex]
    nextY = y + dy[directionIndex] 
    
    tail.append((x,y))
    if nextX < 0 or nextY < 0 or nextX >= n or nextY >= n or board[nextX][nextY] == 2 : 
        break;
    else :
        if board[nextX][nextY] != 1 :
            if len(tail) > 0 :
                tailX, tailY = tail[0]
                board[tailX][tailY] = 0
                tail.pop(0)

        board[nextX][nextY] = 2
        
    x = nextX 
    y = nextY

    if len(direction) > 0 and direction[0][0] == time :
        if direction[0][1] == 'D' :
            directionIndex += 1
            if directionIndex > 3 :
                directionIndex = 0
        else :
            directionIndex -= 1
            if directionIndex < 0 :
                directionIndex = 3;
        direction.pop(0)
    # X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다



print(time)



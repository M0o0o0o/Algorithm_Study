'''
#해당 문제는 '이것이 취업을 위한 코딩 테스트다'의 문제입니다.
1. 바다로 되어 있는 공간에는 갈 수 없다.
2. 현 위치, 방향에서 왼쪽방향부터 갈 곳을 정함.
3. 왼쪽 방향에 존재하면 한 칸 고, 없으면 그 방향에서 끝
4. 만약 네 방향 모두 가본 칸이거나 바다인 경우, 바라보는 방향을 유지한
채로 한 칸 뒤로 가고 1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 
칸이라 뒤로 갈 수 없는 경우 에는 움직임을 멈춘다.

1. 좌표와 방향 입력 받고
2. 동 북 서 남 순으로 dx,dy설정
3. 내가 가본 곳은 2로 설정하자 
4. 얼마나 실패 했는지에 대해서 카운트 필요한 듯 (아니라면 코드로 해결)


'''

#계속 예제 코드의 답이 내 코드로 돌려보면 2가 나왔었는데
#생각해보니 문제의 조건에 의하면 '처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다'라는 조건이 있으면 항상 result = 1로 시작해야 했다!!! ** 문제의 조건을 항상 잘 읽자

n, m = map(int, input().split())
x, y, d = map(int, input().split())
move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
stop = False
maps = list()
result = 1

for i in range(n):
    maps.append(list(map(int, input().split())))


def check_land(x, y):
    global n, m
    if x >= 0 and x < n and y >= 0 and y < m:
        return True
    return False


while True:
    for i in range(4):
        d = (d + 1) % 4
        nx = x + move[d][0]
        ny = y + move[d][1]
        if check_land(nx, ny) and maps[nx][ny] == 0:
            result += 1
            x = nx
            y = ny
            maps[x][y] = 2
            continue
        else:
            if i == 3:
                d = (d + 2) % 4
                nx = x + move[d][0]
                ny = y + move[d][1]
                if check_land(nx, ny) and maps[nx][ny] == 0:
                    result += 1
                    x = nx
                    y = ny
                    maps[x][y] = 2
                    break
                else:
                    stop = True
                    break
            else:
                continue
    if stop:
        break

print(result)
'''
#책에 구현 코드 
n ,m = map(int, input().split())

d = [[0] * m for _ in range(n)]
x,y,direction = map(int, input().split())
d[x][y] = 1 

array = []
for i in range(n) :
  array.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left() :
  global direction
  direction -= 1
  if(direction == -1) :
    directinon = 3

count = 1
turn_time = 0
while True :
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  if d[nx][ny] == 0 and array[nx][ny] == 0 :
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  else :
    turn_time += 1
  
  if turn_time == 4 :
    nx = x - dx[direction]
    ny = y - dy[direction]

    if array[nx][ny] == 0 :
      x = nx
      y = ny
    else:
      break
    turn_time = 0

print(count)
'''

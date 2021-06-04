# https://www.acmicpc.net/problem/18428
# 복도에 나온 학생들이 선생님의 감시에 들키지 않는 것이 목표
# 각 선생님은 자신의 위치에서 상, 하, 좌, 우 감시를 진행, 단, 복도에 장애물이 있으면 선생님은 장애물 뒤편에 숨어 있는 학생 볼 수 없음.
# 또한 아무리 멀리 있더라도 장애물로 막히기 전까지 4가지 방향으로 학생을 모두 볼 수 있다.
# 선생님 T 학생 S 장애물 O

def solution(count):
    global answer
    if count == 3:
        result = check()
        if result == True:
            answer = "YES"
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                solution(count + 1)
                graph[i][j] = 'X'
                if answer == 'YES':
                    return


def check():
    for x, y in teacher:
        mx, my = x, y
        while True:
            mx += dx[0]
            my += dy[0]
            if mx >= 0 and mx < n and my >= 0 and my < n:
                if graph[mx][my] == 'S':
                    return False
                elif graph[mx][my] == 'O':
                    break
            else:
                break

        mx, my = x, y
        while True:
            mx += dx[1]
            my += dy[1]
            if mx >= 0 and mx < n and my >= 0 and my < n:
                if graph[mx][my] == 'S':
                    return False
                elif graph[mx][my] == 'O':
                    break
            else:
                break

        mx, my = x, y
        while True:
            mx += dx[2]
            my += dy[2]
            if mx >= 0 and mx < n and my >= 0 and my < n:
                if graph[mx][my] == 'S':
                    return False
                elif graph[mx][my] == 'O':
                    break
            else:
                break

        mx, my = x, y
        while True:
            mx += dx[3]
            my += dy[3]
            if mx >= 0 and mx < n and my >= 0 and my < n:
                if graph[mx][my] == 'S':
                    return False
                elif graph[mx][my] == 'O':
                    break
            else:
                break

    return True


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer = "NO"
n = int(input())
graph = []

for _ in range(n):
    graph.append(list(input().split()))


teacher = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append((i, j))


solution(0)
print(answer)

# https://www.acmicpc.net/problem/16234
# 인접한 나라 사이에는 국경선이 존재한다.
# 인구 이동은 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다. (재귀적으로 해결)

# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 안 연다.
# 위의 조건에 의해 열어야 하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국격선이 열려 있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.


# BFS를 이용해 풀이

from collections import deque


def solution(x, y, index):
    united = []
    united.append((x, y))
    q = deque()
    q.append((x, y))

    country[x][y] = index  # 현재 연합의 번호 할당
    summary = graph[x][y]
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n and country[nx][ny] == - 1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    country[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))

    for i, j in united:
        graph[i][j] = summary // count


n, l, r = map(int, input().split())

graph = []
division = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

unionGraph = [[0]*n for _ in range(n)]
result = 0

while True:
    country = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if country[i][j] == -1:
                solution(i, j, index)
                index += 1

    if index == n * n:
        break
    result += 1
print(result)

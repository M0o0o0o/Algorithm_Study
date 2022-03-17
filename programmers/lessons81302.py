# 파티션을 만난 경우 더이상 진행할 필요가 없기 때문에 패스
#  빈 테이블을 만난 경우 진행할 수 있따.
# 파티션을 만난 경우 진행하지 않기 때문에 맨해튼 거리 안에서 응시자를 만나면 False 리턴

from collections import deque

n = 5
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def bfs(board, start):
    q = deque([start])
    visited = [[False] * n for _ in range(n)]
    visited[start[0]][start[1]] = True

    while q:
        x, y, d = q.popleft()
        if d == 2:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] == 'P':
                    return False
                if board[nx][ny] == 'O':
                    q.append((nx, ny, d + 1))
    return True


def solution(places):
    ans = []
    for p in places:
        check = 1
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    result = bfs(p, (i, j, 0))
                    if not result:
                        check = 0
        ans.append(check)
    return ans


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
      "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

# https://www.acmicpc.net/problem/10164

def solution(sx, sy, ex, ey):
    dp = [[0 for _ in range(m+1)]for _ in range(n + 1)]
    dp[sx][sy] = 1
    for x in range(sx, ex+1):
        for y in range(sy, ey+1):
            for d in range(2):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx and 0 <= ny:
                    dp[x][y] += dp[nx][ny]
    return dp[ex][ey]


n, m, k = map(int, input().split())
dx, dy = [0, -1], [-1, 0]
ans = 1

if k != 0:
    ans *= solution(1, 1, (k // m) + 1,  k % m) * \
        solution((k//m) + 1, k % m, n, m)
else:
    ans *= solution(1, 1, n, m)
print(ans)

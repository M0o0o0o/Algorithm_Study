# https://www.acmicpc.net/problem/23841

n, m = map(int, input().split())
pt = [list(input()) for _ in range(n)]
for i in range(n):
    d = m-1
    for j in range(m // 2):
        if pt[i][j] != '.':
            pt[i][j+d] = pt[i][j]
        elif pt[i][j+d] != '.':
            pt[i][j] = pt[i][j+d]
        d -= 2
    for j in range(m):
        print(pt[i][j], end='')
    print()

# https://www.acmicpc.net/problem/1063

n, m = 8, 8
k, r, c = input().split()
c = int(c)
ky, kx = ord(k[0]) - 64, int(k[1])
ry, rx = ord(r[0]) - 64, int(r[1])
d = {'R': (0, 1), 'L': (0, -1), 'B': (-1, 0), 'T': (1, 0),
     'RT': (1, 1), 'LT': (1, -1), 'RB': (-1, 1), 'LB': (-1, -1)}


for _ in range(c):
    dd = input()
    dx, dy = d[dd]
    nx, ny = kx + dx, ky + dy
    if 1 <= nx <= n and 1 <= ny <= m:

        if (rx, ry) == (nx, ny):
            if not (1 <= rx + dx <= n and 1 <= ry + dy <= m):
                continue
            rx, ry = rx + dx, ry + dy
        kx, ky = nx, ny

print(chr(ky + 64) + str(kx))
print(chr(ry + 64) + str(rx))

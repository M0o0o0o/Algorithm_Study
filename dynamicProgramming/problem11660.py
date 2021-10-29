# https://www.acmicpc.net/problem/11660

import sys
input = sys.stdin.readline


n, m = map(int, input().split())

lst = [[0] * (n + 1)]

for _ in range(n):
    nums = [0] + [int(x) for x in input().split()]
    lst.append(nums)


for i in range(1, n + 1):
    for j in range(1, n):
        lst[i][j + 1] += lst[i][j]

for j in range(1, n + 1):
    for i in range(1, n):
        lst[i + 1][j] += lst[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(lst[x2][y2] - lst[x1 - 1][y2] - lst[x2][y1 - 1] + lst[x1 - 1][y1 - 1])


for i in range(n+1) :
    print(lst[i])
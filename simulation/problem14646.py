# https://www.acmicpc.net/problem/14646

import sys
input = sys.stdin.readline

n = int(input())
menu = [False for _ in range(n+1)]
cnt, res = 0, 0

for l in list(map(int, input().split())):
    if not menu[l]:
        cnt += 1
        menu[l] = True
        res = max(res, cnt)
        continue
    cnt -= 1
    menu[l] = False

print(res)

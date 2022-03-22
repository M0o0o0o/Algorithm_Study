# https://www.acmicpc.net/problem/1592

import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())

# 현재 받은 횟수가 홀수번이면 자기의 현재 위치에서 시계 방향으로 L번째 있는 사람에게,
# 짝수번이면 현재 위치에서 반시계 방향으로 L번째 사람에게 공은 던진다.

lst = [0] * n
lst[0] = 1
cnt, pos = 0, 0

while True:
    if lst[pos] == m:
        print(cnt)
        break
    if lst[pos] % 2 == 0:
        pos = pos - l + n if pos - l < 0 else pos - l
    else:
        pos = pos + l - n if pos + l >= n else pos + l
    lst[pos] += 1
    cnt += 1

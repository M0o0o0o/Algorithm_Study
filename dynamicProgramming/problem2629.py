# https://www.acmicpc.net/problem/2629

import sys
input = sys.stdin.readline


def scale(chu, n, now, left, right, possible):
    new = abs(left-right)
    if(new not in possible):
        possible.append(new)
    if(now == n):
        return 0
    if(answer[now][new] == 0):
        scale(chu, n, now+1, left+chu[now], right, possible)
        scale(chu, n, now+1, left, right+chu[now], possible)
        scale(chu, n, now+1, left, right, possible)
        answer[now][new] = 1


n = int(input())
chu = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
possible = []
answer = [[0]*15001 for i in range(n+1)]


scale(chu, n, 0, 0, 0, possible)
for i in range(0, len(check)):
    if(check[i] in possible):
        print("Y", end=' ')
    else:
        print("N", end=' ')

# https://www.acmicpc.net/problem/10942
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
m = int(input())
dp = [[0] * n for _ in range(n)]

for i in range(n) :
    dp[i][i] = 1

for i in range(n-1) :
    if lst[i] == lst[i+1] :
        dp[i][i+1] = 1

for l in range(2,n) :
    for i in range(n-l) :
        if lst[i] == lst[i+l] and dp[i+1][i+l-1] == 1 :
            dp[i][i+l] = 1
for _ in range(m) :
    s, e = map(int,input().split())
    print(dp[s-1][e-1])


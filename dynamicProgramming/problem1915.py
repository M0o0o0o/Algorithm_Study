# https://www.acmicpc.net/problem/1915

import sys 
input = sys.stdin.readline

n, m = map(int,input().split())
lst = []
dp = [[0] * m for _ in range()]
for _ in range(n) :
    lst.append(list(map(int, list(input().rstrip()))))

result = 0
for i in range(n) :
    for j in range(m) :
        if i == 0 or j == 0 :
            dp[i][j] = lst[i][j] 
        elif lst[i][j] == 0 : 
            dp[i][j] = 0 
        else : dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        result = max(result, dp[i][j])

print(result ** 2)
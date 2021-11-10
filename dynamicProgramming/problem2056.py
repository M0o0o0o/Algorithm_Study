# https://www.acmicpc.net/problem/2056

import sys 
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
for i in range(1,n+1) :
    lst = list(map(int, input().split()))
    for work in lst[1:] :
        dp[i] = max(dp[i], dp[work] + lst[0])
        
print(max(dp))
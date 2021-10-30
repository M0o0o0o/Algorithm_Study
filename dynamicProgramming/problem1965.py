# https://www.acmicpc.net/problem/1965

n = int(input())
lst = list(map(int,input().split()))
dp = [1] * n 

for i in range(n) :
    for j in range(i-1, -1, -1) :
        if lst[i] > lst[j] and dp[i] < dp[j] + 1 :
            dp[i] = dp[j] + 1

print(max(dp))
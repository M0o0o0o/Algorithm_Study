# https://www.acmicpc.net/problem/13301

def recur(num):
    if dp[num] != 0:
        return dp[num]
    dp[num] = recur(num-1) + recur(num-2)
    return dp[num]


dp = [0] * 81
dp[1], dp[2], dp[3] = 4, 6, 10
n = int(input())
print(recur(n))

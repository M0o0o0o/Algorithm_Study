# https://www.acmicpc.net/problem/1793


dp = [0] * 251
dp[1], dp[2] = 1, 3

for i in range(3, 251):
    dp[i] = dp[i-1] + (dp[i-2] * 2)
while True:

    try:
        n = int(input())
        if n == 0:
            print(1)
            continue
        print(dp[n])

    except:
        break

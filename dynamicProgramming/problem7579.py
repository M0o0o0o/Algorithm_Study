# https://www.acmicpc.net/problem/7579

n, m = map(int, input().split())
apps = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(sum(costs) + 1)]for _ in range(n+1)]
result = sum(costs)

for i in range(1, n+1):
    app = apps[i]
    cost = costs[i]

    for j in range(1, sum(costs) + 1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(app + dp[i-1][j-cost], dp[i-1][j])

        if dp[i][j] >= m:
            result = min(result, j)

if m != 0:
    print(result)
else:
    print(0)

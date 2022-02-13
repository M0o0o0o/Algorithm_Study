# https://www.acmicpc.net/problem/17173

n, m = map(int, input().split())
items = list(map(int, input().split()))
ans = 0
for i in range(1, n+1):
    for item in items:
        if i % item == 0:
            ans += i
            break
print(ans)

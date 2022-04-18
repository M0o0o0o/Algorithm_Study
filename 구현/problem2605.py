# https://www.acmicpc.net/problem/2605

n = int(input())
order = [i for i in range(1, n+1)]
pick = list(map(int, input().split()))

for i in range(n):
    p = pick[i]
    if p == 0:
        continue
    order = order[0:i-p] + [order[i]] + order[i-p:i] + order[i+1:]
print(*order)

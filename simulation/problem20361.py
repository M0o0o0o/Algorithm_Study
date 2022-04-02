# https://www.acmicpc.net/problem/20361

n, x, k = map(int, input().split())
for _ in range(k):
    a, b = map(int, input().split())
    if x in [a, b]:
        if x == a:
            x = b
        else:
            x = a
print(x)

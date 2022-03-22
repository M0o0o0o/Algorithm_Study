# https://www.acmicpc.net/problem/10810

n, m = map(int, input().split())
lst = [0] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        lst[i] = c

print(*lst[1:])

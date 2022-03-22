# https://www.acmicpc.net/problem/10813

n, m = map(int, input().split())
lst = [i for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    lst[a], lst[b] = lst[b], lst[a]

print(*lst[1:])

# https://www.acmicpc.net/problem/5721

while True:
    n, m = map(int, input().split())
    if n + m == 0:
        break
    graph = [0] * m + [list(map(int, input().split())) for _ in range(n)]

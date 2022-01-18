# https://www.acmicpc.net/problem/24313

# 1
(a1, a2), c, N = map(int, input().split()), int(input()), int(input())
lst = [1 if (a1 * n) + a2 <= c * n else 0 for n in range(N, 101)]
print(1) if lst.count(0) == 0 else print(0)

# 2
(a1, a2), c, N = map(int, input().split()), int(input()), int(input())
print(1) if (a1 + (a2 / N if a2 > 0 else a2 / 100) <= c) else print(0)

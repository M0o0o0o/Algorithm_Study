# https://www.acmicpc.net/problem/23812

n = int(input())
[print('@' * n + '   ' * n + '@' * n) for _ in range(n)]
[print('@@@@@' * n) for _ in range(n)]
[print('@' * n + '   ' * n + '@' * n) for _ in range(n)]
[print('@@@@@' * n) for _ in range(n)]
[print('@' * n + '   ' * n + '@' * n) for _ in range(n)]

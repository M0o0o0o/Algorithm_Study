# https://www.acmicpc.net/problem/23808

n = int(input())
for _ in range(2 * n) :
    print('@' * n + '   ' * n + '@' * n)
for _ in range(n) :
    print('@@@@@' * n)
for _ in range(n) :
    print('@' * n + '   ' * n + '@' * n)
for _ in range(n) :
    print('@@@@@' * n)
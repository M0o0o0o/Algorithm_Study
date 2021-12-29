# https://www.acmicpc.net/problem/23806

n = int(input())
for _ in range(n) :
    print('@@@@@' * n)
for _ in range(3 * n)  :
    print('@' * n + '   ' * n + '@' * n )
for _ in range(n) :
    print('@@@@@' * n)

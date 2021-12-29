# https://www.acmicpc.net/problem/23802

n = int(input())
for _ in range(n) :
    print('@@@@@' * n)
for _ in range(4 * n) :
    print('@' * n)
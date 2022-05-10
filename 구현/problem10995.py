# https://www.acmicpc.net/problem/10995

n = int(input())
one, two = ' ', '*'
for i in range(1, n + 1):
    one, two = two, one
    print((one + two) * n)

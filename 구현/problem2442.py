# https://www.acmicpc.net/problem/2442

n = int(input())
for i in range(n-1, -1, -1) :
    for _ in range(i) : print(' ', end = '')
    print('*' * (((n - i) * 2) - 1))

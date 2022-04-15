# https://www.acmicpc.net/problem/10990

n = int(input())
for i in range(n):
    print(' ' * (n-i-1), end='')
    print('*', end='')
    if i > 0:
        print(' ' * (i * 2 - 1) + '*', end='')
    print()

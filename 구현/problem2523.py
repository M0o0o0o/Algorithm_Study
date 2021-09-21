# https://www.acmicpc.net/problem/2523

n = int(input())

for i in range(1, n) :
    print('*' * i , end = '')
    for _ in range(n-i) : print(' ', end = '')
    for _ in range(n-i) : print(' ', end = '')
    print('*' * i , end = '')
    print()
for i in range(n, 0, -1) :
    print('*' * i , end = '')
    for _ in range(n-i) : print(' ', end = '')
    for _ in range(n-i) : print(' ', end = '')
    print('*' * i , end = '')
    print()
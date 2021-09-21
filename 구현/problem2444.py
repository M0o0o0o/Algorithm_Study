# https://www.acmicpc.net/problem/2444

n = int(input())

for i in range(1, n) :
    for _ in range(n-i) : print(' ', end = '')
    print('*' * (2 * i - 1)   , end = '')
    print()
for i in range(n, 0, -1) :
    for _ in range(n-i) : print(' ', end = '')
    print('*' * (2 * i - 1)   , end = '')
    print()
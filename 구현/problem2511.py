# https://www.acmicpc.net/problem/2511

import sys
input = sys.stdin.readline
a, b = list(map(int, input().split())), list(map(int, input().split()))
ac, bc, d, last = 0, 0, 0, 'A'

for i in range(10):
    if a[i] > b[i]:
        ac += 3
        last = 'A'
    elif a[i] < b[i]:
        bc += 3
        last = 'B'
    else:
        d += 1
        ac += 1
        bc += 1
print(ac, bc)
if ac == bc and d != 10:
    print(last)
elif ac == bc and d == 10:
    print('D')
else:
    print('A' if ac > bc else 'B')

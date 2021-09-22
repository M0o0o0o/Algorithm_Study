# https://www.acmicpc.net/problem/2522

n = int(input())

for i in range(1, n+1) :
    for j in range(n-i) : print(' ',end ='')
    for k in range(i) : print('*', end = '')
    print()
for i in range(n-1, 0, -1) :
    for j in range(n-i) : print(' ',end ='')
    for k in range(i) : print('*', end = '')
    print()

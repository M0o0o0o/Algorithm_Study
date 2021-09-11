# https://www.acmicpc.net/problem/2441

n = int(input())

for i in range(n,-1,-1) :
    for k in range(n - i) :
        print(' ', end ='')
    for j in range(i) :
        print('*', end = '')
    print() 
# https://www.acmicpc.net/problem/2440

n = int(input())

for i in range(n,-1,-1) :
    for j in range(i) :
        print('*', end = '')
    print() 
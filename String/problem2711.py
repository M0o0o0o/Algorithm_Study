# https://www.acmicpc.net/problem/2711

for _ in range(int(input())) : 
    i,a = input().split(' ')
    i = int(i) -1
    print(a[:i] + a[i+1:])
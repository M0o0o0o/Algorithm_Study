# https://www.acmicpc.net/problem/3003

lst = [1,1,2,2,2,8]
buf = list(map(int, input().split()))

for i in range(6) :
    print(lst[i] - buf[i], end = ' ')
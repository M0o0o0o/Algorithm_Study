# https://www.acmicpc.net/problem/5635

n = int(input())
lst = []

for _ in range(n) :
    buf = list(input().split(' '))
    for i in range(1,4) : buf[i] = int(buf[i])
    lst.append(tuple(buf))     

lst.sort(key=lambda x:(x[3], x[2], x[1]));
print(lst[-1][0])
print(lst[0][0])
    
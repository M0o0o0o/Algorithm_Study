# https://www.acmicpc.net/problem/2501

n, k = map(int,input().split())

lst = []
for i in range(1, n+1) :
    if n % i == 0 :
        lst.append(i)

if len(lst) >= k :
    print(lst[k-1])
else :
    print(0)
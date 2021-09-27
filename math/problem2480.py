# https://www.acmicpc.net/problem/2480

lst = list(map(int,input().split()))
answer = max(lst) * 100
for num in lst :
    if lst.count(num) == 2 :
        answer= 1000 + (num * 100)
    if lst.count(num) == 3 :
        answer = 10000 + (num * 1000)

print(answer)
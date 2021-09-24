# https://www.acmicpc.net/problem/2953

answer = [0,0]

for i in range(1, 6) :
    lst = list(map(int,input().split()))
    if answer[1] < sum(lst) :
        answer = [i, sum(lst)]

print(answer[0], answer[1])

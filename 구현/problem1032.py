# https://www.acmicpc.net/problem/1032

n = int(input())
lst = []
answer = ""

for _ in range(n) :
    lst.append(input())

for i in range(len(lst[0])) :
    check = True
    for j in range(n - 1) :
        if lst[j][i] != lst[j+1][i] :
            check = False
    if check :
        answer += lst[0][i]
    else :
        answer += '?'

print(answer)
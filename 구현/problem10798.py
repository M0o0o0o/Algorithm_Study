# https://www.acmicpc.net/problem/10798

lst = [[None] * 15 for _ in range(5)]

for i in range(5) :
    string = list(input())
    for j in range(len(string)) :
        lst[i][j] = string[j]

for j in range(15) :
    for i in range(5) :
        if lst[i][j] is not None :
            print(lst[i][j], end ='')

# https://www.acmicpc.net/problem/2775

lst = [[0] * 15 for _ in range(15)]
for i in range(1, 15) :
    lst[0][i] = i

for i in range(1, 15) :
    for j in range(1, 15) :
        for k in range(1, j+1) :
            lst[i][j] += lst[i-1][k] 

for i in range(int(input())) :
    k = int(input())
    n = int(input())
    print(lst[k][n])

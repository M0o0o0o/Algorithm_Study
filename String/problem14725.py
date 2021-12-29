# https://www.acmicpc.net/problem/14725

n = int(input())
ant = []

for _ in range(n) :
    lst = list(input().split())
    ant.append(lst[1:])
ant.sort()

for i in range(n) :
    if i == 0 : 
        for j in range(len(ant[i])) :
            print('--' * j + ant[i][j])
    else :
        count = -1
        for j in range(len(ant[i])) :
            if len(ant[i-1]) <= j or ant[i-1][j] != ant[i][j] : 
                break
            else : 
                count = j
        for j in range(count + 1, len(ant[i])) :
            print('--' * j + ant[i][j])
        
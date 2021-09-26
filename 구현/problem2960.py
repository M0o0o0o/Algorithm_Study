# https://www.acmicpc.net/problem/2960

n, k = map(int,input().split())
lst = [True] * (n+1)
count = 0 

for i in range(2, n+1) :
    for j in range(i, n+1, i) :
        if lst[j] :
            lst[j] = False
            count += 1
            if count == k :
                print(j)
                break
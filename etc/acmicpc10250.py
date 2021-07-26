# https://www.acmicpc.net/problem/10250

import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    h, w, n = map(int, input().split())
    h += 1
    w += 1
    hotel = [[True] * w for _ in range(h)]
    count = 0 

    for j in range(1, w) :
        for i in range(1, h):
            if hotel[i][j] :
                count += 1
                hotel[i][j] = False
            
            if count == n :
                if j < 10 :
                    print(str(i) + '0' + str(j))
                else :
                    print(str(i) + str(j))

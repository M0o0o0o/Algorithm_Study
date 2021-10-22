# https://www.acmicpc.net/problem/1431

import sys 
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n) :
    serial = input().strip('\n')
    count = 0 
    for i in serial :
        if '0' <= i <= '9' :
            count += int(i)

    lst.append((len(serial), count, serial))
lst.sort(key=lambda x:(x[0], x[1], x[2]));


for i in lst :
    print(i[2])
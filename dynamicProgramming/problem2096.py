# https://www.acmicpc.net/problem/2096

import sys
input = sys.stdin.readline

n = int(input())
big, small = [0,0,0], [0,0,0]

for i in range(n) :
    
    lst = list(map(int,input().split()))
    lst2 = lst[:]

    lst[0] += max(big[0], big[1])
    lst[1] += max(big[0], big[1], big[2])
    lst[2] += max(big[1], big[2])
    big = lst[:]

    lst2[0] += min(small[0], small[1])
    lst2[1] += min(small[0], small[1], small[2])
    lst2[2] += min(small[1], small[2])
    small = lst2[:]


    
print(max(big), min(small))


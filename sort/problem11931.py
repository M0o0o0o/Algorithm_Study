# https://www.acmicpc.net/problem/11931

import sys 
input = sys.stdin.readline

lst = []
n = int(input())

for _ in range(n) :
    lst.append(int(input()))

lst.sort(reverse=True)

for l in lst :
    print(l)
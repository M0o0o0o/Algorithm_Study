# https://www.acmicpc.net/problem/2752

lst = list(map(int,input().split()))
lst.sort()

for i in lst :
    print(i, end = ' ')
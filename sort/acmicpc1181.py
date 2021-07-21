# https://www.acmicpc.net/problem/1181

import sys
input = sys.stdin.readline

n = int(input()) 
arr = set()

for _ in range(n) :
    arr.add(input().replace('\n', ''))

arr = list(arr)

for i in range(len(arr)) :
    arr[i] = (len(arr[i]), arr[i])

arr.sort(key=lambda x:(x[0], x[1]));

for l, value in arr :
    print(value)

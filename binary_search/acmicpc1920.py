# https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

m = int(input())
search = list(map(int, input().split()))

for s in search :
    start = 0 
    end = n-1
    while start <= end :
        mid = (start + end) // 2
        if lst[mid] < s :
            start = mid + 1 
        elif lst[mid] > s :
            end = mid -1
        else :
            print('1')
            break

    if start > end :
        print('0')


# https://www.acmicpc.net/problem/17201

n = int(input())
s = input().strip('\n')
if s.count('11') > 0 or s.count('22') > 0:
    print('No')
else:
    print('Yes')

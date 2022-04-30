# https://www.acmicpc.net/problem/13752

n = int(input())
lst = [int(input()) for _ in range(n)]
for num in lst:
    print('=' * num)

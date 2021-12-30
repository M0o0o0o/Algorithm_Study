# https://www.acmicpc.net/problem/16212

n = int(input())
[print(l, end = ' ') for l in sorted(list(map(int, input().split())))]
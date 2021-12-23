# https://www.acmicpc.net/problem/11659
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [0] + list(map(int, input().split()))
total = [0] * (n+1)

for i in range(1, n+1):
    total[i] += lst[i] + total[i-1]

for _ in range(m):
    s, e = map(int, input().split())
    print(total[e] - total[s-1])

# https://www.acmicpc.net/problem/11945

n, m = map(int, input().split())
pan = [input().strip('\n') for _ in range(n)]
for i in range(n):
    print(pan[i][::-1])

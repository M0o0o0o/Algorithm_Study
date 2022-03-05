# https://www.acmicpc.net/problem/9625

n = int(input())
a, b = 1, 0

for _ in range(n):
    bufA, bufB = 0, 0
    bufA += b
    bufB += b + a
    a, b = bufA, bufB

print(a, b)

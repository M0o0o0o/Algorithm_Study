# https://www.acmicpc.net/problem/1026

n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

answer = [a[i] * b[i] for i in range(n)]
print(sum(answer))

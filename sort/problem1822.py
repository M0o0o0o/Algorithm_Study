# https://www.acmicpc.net/problem/1822

n, m = map(int, input().split())
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
C = a.difference(b)
print(len(C))
for c in sorted(list(C)) :
    print(c, end = ' ')


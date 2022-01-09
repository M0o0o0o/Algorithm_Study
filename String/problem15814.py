# https://www.acmicpc.net/problem/15814

s = list(input())
for _ in range(int(input())) :
    a, b = map(int, input().split())
    s[a], s[b] = s[b], s[a]
print(''.join(s))
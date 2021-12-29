# https://www.acmicpc.net/problem/23809

n = int(input())

for i in range(n) :
    print('@' * n + '   ' * n + '@' * n)
for i in range(n) :
    print('@' * n + '  ' * n + '@' * n)
for i in range(n) : 
    print('@@@' * n)
for i in range(n) :
    print('@' * n + '  ' * n + '@' * n)
for i in range(n) :
    print('@' * n + '   ' * n + '@' * n)

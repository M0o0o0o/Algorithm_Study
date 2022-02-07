# https://www.acmicpc.net/problem/1568

n = int(input()) - 1
c = 2
ans = 1

while n > 0:
    if n < c:
        c = 1
    n -= c
    c += 1
    ans += 1

print(ans)

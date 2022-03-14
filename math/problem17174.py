# https://www.acmicpc.net/problem/17174

n, m = map(int, input().split())
ans = n
while n // m > 0:
    n //= m
    ans += n

print(ans)

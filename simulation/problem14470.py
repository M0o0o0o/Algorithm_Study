# https://www.acmicpc.net/problem/14470

a, b, c, d, e = int(input()), int(input()), int(
    input()), int(input()), int(input())
ans = 0
# a to b
if a < 0:
    ans += abs(a) * c
    ans += d
    a = 0

ans += (b-a) * e
print(ans)

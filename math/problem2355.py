# https://www.acmicpc.net/problem/2355

a, b = map(int, input().split())
a, b = min(a, b), max(a, b)


def f(n):
    return (n*(n+1))//2


if a == b:
    print(a)
elif a <= 0 and b >= 0:
    print(f(b) - f(-a))
elif b <= 0:
    print(-(f(-a) - f(-b-1)))
else:
    print(f(b) - f(a-1))

# https://www.acmicpc.net/problem/5532

l, a, b, c, d = int(input()), int(input()), int(input()), int(input()), int(input())
print(l - max((a // c + (1 if a % c > 0 else 0)), (b // d + (1 if b % d > 0 else 0))))
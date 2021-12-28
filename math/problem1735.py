# https://www.acmicpc.net/problem/1735

import math
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
up = a1 * b2 + a2 * b1
down = b1 * b2
my = math.gcd(up, down)
up //= my
down //= my
print(up, down)
# https://www.acmicpc.net/problem/2869
import math
a, b, v = map(int, input().split())

result = ((v-a) / (a-b))

print(math.ceil(result) + 1)
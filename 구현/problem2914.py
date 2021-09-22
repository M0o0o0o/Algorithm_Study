# https://www.acmicpc.net/problem/2914

import math
a, b = map(int,input().split())
for num in range(a*b, -1, -1) :
    if math.ceil(num / a) != b :
        print(num + 1)
        break   
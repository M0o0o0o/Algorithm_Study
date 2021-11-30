# https://www.acmicpc.net/problem/3135

import sys; input = sys.stdin.readline
import math
a, b = map(int, input().split())
lst = [abs(a-b)-1]
[lst.append(abs(int(input())-b)) for _ in range(int(input()))]
print(min(lst) + 1)    
    
# https://www.acmicpc.net/problem/11404

import heapq
import sys

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

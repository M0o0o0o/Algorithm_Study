# https://www.acmicpc.net/problem/2161

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque([i for i in range(1, n+1)])
ans = []

while len(q) > 1 : 
    ans.append(q.popleft())
    q.append(q.popleft())

ans.append(q.popleft())
for a in ans : 
    print(a, end = ' ')
# https://www.acmicpc.net/problem/12761

from collections import deque

a, b, start, end = map(int, input().split())
visited = [False for i in range(100001)]

q = deque([(start, 0)])
visited[start] = True

while q:
    loc, count = q.popleft()
    if loc == end:
        print(count)
        break
    for m in [(loc * a) - loc, (loc * b) - loc, a, b, -a, -b, 1, -1]:
        next_loc = m + loc
        if 0 <= next_loc <= 100000 and not visited[next_loc]:
            q.append((next_loc, count + 1))
            visited[next_loc] = True

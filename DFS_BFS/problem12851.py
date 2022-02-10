# https://www.acmicpc.net/problem/12851

from collections import deque

n, k = map(int, input().split())
visited = [-1 for _ in range(100001)]
count = [0 for _ in range(100001)]

q = deque([n])
visited[n] = 0
count[n] = 1

while q:
    position = q.popleft()
    for newP in [position + 1, position-1, position * 2]:
        if 0 <= newP < 100001:
            if visited[newP] == -1:
                visited[newP] = visited[position] + 1
                count[newP] = count[position]
                q.append(newP)
            else:
                if visited[newP] == visited[position] + 1:
                    count[newP] += count[position]

print(visited[k])
print(count[k])

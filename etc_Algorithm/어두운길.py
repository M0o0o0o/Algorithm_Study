from collections import deque

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x]) 
    return parent[x] 

def union(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b 


n, m = map(int, input().split())

parent = [0] * n 

for i in range(n) :
    parent[i] = i

roads = []

for _ in range(m) :
    x, y, z  = map(int,input().split())
    roads.append((z, x, y))

roads.sort()

result = 0

for road in roads :
    cost, x, y = road
    if find_parent(parent, x) != find_parent(parent, y) :
        union(parent, x, y) 
    else : 
        result += cost

print(result)

# 7 11
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11

# https://www.acmicpc.net/problem/1043

def find(parent, x) :
    if x != parent[x] :
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b) :
    a = find(parent,a)
    b = find(parent,b)
    if a < b :
        parent[b] = a 
    else :
        parent[a] = b

n, m = map(int,input().split())
parent = [0] * (n+1)
parties = [list(map(int, input().split()))[1:] for _ in range(m)]
result = 0

lie = list(map(int, input().split()))[1:]
for i in range(n+1) :
    parent[i] = i
    
if not lie :
    print(m) 
    exit(0)

for i in range(0, len(lie)) :
    union(parent, 0, lie[i])

for _ in range(m) :
    for party in parties :
        flag = False
        for p in party :
            if parent[p] == 0 :
                flag = True
                break
        if flag : 
            for p in party :
                union(parent, 0, p)

for p in parties :
    flag = True
    for person in p :
        if parent[person] == 0 :
            flag = False

    if flag : result += 1

print(result)


             
            

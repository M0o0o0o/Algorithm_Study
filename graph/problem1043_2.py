import sys
input = sys.stdin.readline

n, m = map(int, input().split())
witness = set(list(map(int,input().split()))[1:])
party = [set(list(map(int,input().split()))[1:]) for _ in range(m)]
result = [1 for _ in range(m)]

for _ in range(m) :
    for i in range(m) :
        if witness & party[i] :
            result[i] = 0
            witness = witness | party[i]
print(sum(result))
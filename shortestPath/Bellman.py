import sys
input = sys.stdin.readline
INF = int(1e9)


def bf(start) :
    dist[start ] = 0 
    for i in range(n) :
        for j in range(m) :
            cur, next, cost = edges[j][0], edges[j][1], edges[j][2] 
            if dist[cur] != INF and dist[next] > dist[cur] + cost :
                dist[next] = dist[cur] + cost
                # n번째에도 값이 갱신된다면 음수 순환이 존재 
                if i == n - 1 :
                    return True
    return False

n, m = map(int,input().split())
edges = []
dist = [INF] * (n+1)

for _ in range(m) :
    a, b, c = map(int,input().split())
    edges.append((a,b,c))

cycle = bf(1)

if cycle : 
    print('-1')
else :
    for i in range(2, n+1) :
        if dist[i] == INF  :
            print('-1')
        else :
            print(dist[i])
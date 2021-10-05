from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indgree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v + 1)]


# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indgree[b] += 1

# 위상 정렬 함수 
def topology_sort():
    result = []
    q = deque()
# 처음 시작할 때는 진입차수가 0인 노드를 큐에 append
    for i in range(1, v + 1):
        if indgree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indgree[i] -= 1
            if indgree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()

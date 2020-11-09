'''
다익스트라 최단 경로 알고리즘은 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘이다. 다익스트라 최단 경로 알고리즘은 '음의 간선'이 없을 때 정상적으로 동작한다. 또한 다익스트라 최단 경로 알고리즘은 기본적으로 그리기 알고리즘으로 분류된다. 매번 '가장 비용이 적은 노드'를 선택해서 임의의 과정을 반복하기 때문이다. 

다익스트라 최단 경로 알고리즘에서는 '방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드를 선택'하는 과정을 반복하는데, 이렇게 선택된 노드는 '최단 거리'가 완전히 선택된 노드이므로, 더 이상 알고리즘을 반복해도 최단 거리가 줄어들지 않는다. 


동작 과정
1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다. 
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다. 
5. 위 과정에서 3, 4번을 반복한다. 
'''

# 방법 1 시간 복잡도 (v^2)
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수 
n, m = map(int, input().split())
#시작 노드 번호를 입력받기
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보는 담는 리스트를 만들기
graph = [[] for i in range(n+1)]

#방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

#모든 간선 정보를 입력받기
for _ in range(m) :
  a, b, c = map(int,input().split())
#a번 노드에서 b번 노드로 가는 비용이 c라는 의미
  graph[a].append((b,c))

#방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node() :
  min_value = INF
  index = 0 
  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i] :
      min_value = distance[i]
      index = i
    return index

def dijkstra(start) :
  #시작 노드에 대해서 초기화
  distance[start] = 0
  visited[start] = True
  for j in graph[start] :
    distance[j[0]] = j[1]
#시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
  for i in range(n-1) :
    now = get_smallest_node()
    visited[now] = True
#현재 노드와 연결된 다른 노드를 확인
    for j in graph[now] :
      cost = distance[now] + j[1]
#현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 
      if cost < distance[j[0]] :
        distance[j[0]] = cost

dijkstra(sum)

for i in range(1, n+1) :
  if distance[i] == INF :
    print("INFINITY")
  else :
    print(distance[i])


#개선된 다익스트라 알고리즘
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
  a, b, c = map(int,input().split())
  graph[a].append((b,c))

def dijkstra2(start) :
  q  = []
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q :
   dist, now = heapq.heappop(q)
   if distance[now] < dist :
    continue
    for i in graph[now] :
      cost = dist + i[1]
      if cost < distance[i[0]] :
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra2(start)

for i in range(1, n+1) :
  if distance[i] == INF :
    print("INFINITY")
  else :
    print(distance[i])


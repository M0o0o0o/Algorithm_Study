#해당 문제는 '이것이 취업을 위한 코딩 테스트다'의 문제입니다.
#입력 조건이나 출력 조건은 생략했습니다. 
'''
어떤 나라에는 N개의 도시가 있다. 그리고 각 도시는 보내고자 하는 메시지가 있는 경우, 다른 도시에 전보를 보내서 다른 도시로 해당 메시지를 전송할 수 있다. 하지만 X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면, 도시 X에서 Y로 향하는 통로나 설치되어 있어야 한다. 예를 들어 X에서 Y로 향하는 통로는 있지만, Y에서 X로 향하는 통로가 없다면 Y는 X로 메시지를 보낼 수 없다. 또한 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다.

어느 날 C라는 도시에서 위급 상황이 발생했다. 그래서 최대한 많은 도시로 메시지를 보내고자 한다. 메시지는 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다. 각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇 개이며 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n, m, c = map(int, input().split())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m) :
  x, y, z = map(int,input().split())
  graph[x].append((y,z))

def dijkstra(c) :
  q = []
  distance[c] = 0
  heapq.heappush(q, (0, c))

  while q : 
    dist, now = heapq.heappop(q)
    if distance[now] < dist :
      continue
    
    for i in graph[now] :
      cost = dist + i[1]
      if cost < distance[i[0]] : 
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
time = 0

for i in distance :
  if i != INF:
    count += 1 
    time = max(time, i) 

print(count-1,  time) 

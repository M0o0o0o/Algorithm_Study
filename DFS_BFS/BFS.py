'''
BFS는 자료구조는 아니지만, 탐색하는 기법으로 따로 나누기 애매해서
자료구조 파트에 넣었습니다.

BFS(Breadth First Search)는 너비 우선 탐색으로 가까운 노드부터 탐색하는 알고리즘 입니다. DFS가 시작 노드를 기준으로 가장 멀리 있는 노드를 우선으로 탐색하는 방식이었다면, BFS는 큐를 이용해 가까운 노드부터 멀리 퍼져 나가는 방식입니다.

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 합니다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
'''

# BFS 구현

from collections import deque

def bfs(graph, start, visited) :
  queue = deque([start]) # 덱을 이용한 큐를 구현 
 
  visited[start] = True # 방문 처리 한다.
  while queue : 
    v = queue.popleft() 
    print(v, end = ' ')
    for i in graph[v] :
      if not visited[i] :
        queue.append(i)
        visited[i] = True

graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)

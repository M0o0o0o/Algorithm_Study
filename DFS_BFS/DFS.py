'''
DFS는 자료구조는 아니지만, 탐색하는 기법으로 따로 나누기 애매해서
자료구조 파트에 넣었습니다.!!! 

DFS(Depth First Search)는 깊이 우선 탐색으로 스택을 이용해 구현합니다.
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 합니다.
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 있다면, 그 인접 노드를 스택에 넣고 방문 처리를 합니다. 방문하지 않은 인접 노드가 없다면 스택에서 최상단 노드를 꺼냅니다
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복합니다
'''

#DFS 구현 

# 설명에는 스택을 사용한다고 했지만, 재귀 함수의 성질을 이용해 구현하고 있습낟. 
# v = 시작 노드, visited = 방문 처리를 위한 리스트 
def dfs(graph, v, visited) :
  visited[v] = True  #노드 방문 처리 
  print(v, end = ' ') 
  for i in graph[v] :
    if not visited[i]:
      dfs(graph, i, visited)


# 인접 행렬 
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

dfs(graph, 1, visited)
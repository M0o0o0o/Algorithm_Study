'''
그래프를 표현하는 방법에는 두 가지가 있다.
인접행렬, 인접리스트 방식이 있는데, 인접행렬 방식은 2차원 배열을 
이용해 구현하는데, 파이썬에서는 리스트로 구현할 수 있다.
메모리 측면에서는 조금 손해를 볼 수 있지만, 특정 노드와의 관계를 찾을 때는 효율적이다

반대로, 인접리스트는 연결리스트를 이용해 구현하기 때문에 특정 노드를 
찾는 경우 리스트를 모두 순회해야 하기 때문에 속도 면에서 다소 느릴 수 있지만, 모든 그래프를 탐색해야 하는 경우 메모리의 효율을 높일 수 있다. 
'''

#인접행렬
INF = 999999999

graph_1 = [
  [0,7,5],
  [7,0,INF],
  [5,INF,0]
]

print(graph_1)

#인접 리스트

graph = [[] for _ in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))
graph[2].append((0,5))

print(graph)

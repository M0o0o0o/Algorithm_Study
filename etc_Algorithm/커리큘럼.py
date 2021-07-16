#해당 문제는 '이것이 취업을 위한 코딩 테스트다'의 문제입니다.
'''
모든 강의는 1번부터 N번까지의 번호를 가진다.
또한 동시에 여러 개의 강의를 들을 수 있다고 가정한다.
동빈이가 듣고자 하는 N개의 강의 정보가 주어졌을 때 , 
N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 각각 출력하는
프로그램을 작성하시오.
'''

from collections import  deque
import copy

v = int(input())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]
time = [0] * (v+1)

for i in range(1, v+1) :
  data = list(map(int, input().split()))
  time[i] = data[0]
  for x in data[1:-1] :
    indegree[i] += 1
    graph[x].append(i)

def topology_sort() :
  result = copy.deepcopy(time)
  q = deque()
  for i in range(1, v+1) :
    if indegree[i] == 0 :
      q.append(i)
  
  while q:
    now = q.popleft()
    for i in graph[now] :
      result[i] = max(result[i], result[now] + time[i])
      indegree[i] -=1 
      if indegree[i] == 0 :
        q.append(i)

  for i in range(1, v+1) :
    print(result[i])

topology_sort()
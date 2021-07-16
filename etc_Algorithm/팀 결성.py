#해당 문제는 '이것이 취업을 위한 코딩 테스트다'의 문제입니다.
'''
학교에서 학생들에서 0번부터 N번까지의 번호를 부여했다. 처음에는 모든 학생이 서로 다른 팀으로 구분되어, 총 N+1개의 팀이 존재한다. 이때 선생님은 '팀 합치기' 연산과 '같은 팀 여부 확인' 연산을 사용할 수 있다.

1. '팀 합치기'연산은 두 팀을 합치는 연산이다.
2. '같은 팀 여부 확인' 연산은 특정한 두 학생이 같은  팀에 속하는지를 확인하는 연산이다.

선생님이 M개의 연산을 수행할 수 있을 때, '같은 팀 여부 확인' 연산에 대한 연산 결과를  출력하는 프로그램을 작성하시오.
'''
def find_parent(parent, a) :
  if parent[a] != a :
    parent[a] = find_parent(parent, parent[a])
  return parent[a]

def union_parent(parent, a, b) :
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b :
    parent[b] = a
  else :
    parent[a] = b

n, m = map(int, input().split())

parent = [0] * (n+1)

for i in range(1, n+1) :
  parent[i] = i

for _ in range(m) :
  n, a, b = map(int, input().split())
  if n == 0 :
    union_parent(parent,a,b) 
  else : 
    if find_parent(parent, a) == find_parent(parent, b) :
      print("YES")
    else :
      print("NO")
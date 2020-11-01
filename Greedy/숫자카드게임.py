'''
1. 숫자가 쓰인 카드들이 n x m 형태로 놓여 있다. 이 때 n은 행의 개수, m은 열의 개수
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택
3. 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다
4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다
'''

n, m = map(int, input().split())
result = 0 
for i in range(n) :
  data = list(map(int, input().split()))
  min_value = min(data)
  if result < min_value :
    result = min_value

print(result) 


'''
내가 생각한 문제 해결 방법은 행을 선택하면 가장 작은 숫자를 선택해야 하는 것이 문제의 조건이기
때문에 행을 한 줄씩 입력 받을 때마다 해당 행에서 가장 작은 값을 찾아내서 
그 작은 값들 중에서 가장 큰 값을 갱신하는 방식으로 해결하려고 생각했다. 
'''
'''
#답안 예시
n, m = map(int, input().split())

result = 0
for i in range(n) :
  data = list(map(int,input().split()))
  min_value = min(data)

  result = max(result, min_value)

print(result)

#답안 예시2 
n, m = map(int,input().split())

result = 0

for i in range(n) :
  data = list(map(int,input().split()))
  min_value = 10001
  for a in data :
    print(a)
    min_value = min(min_value, a)
  result = max(result, min_value)
print(result)
'''
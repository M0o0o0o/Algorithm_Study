#해당 문제는 '이것이 취업을 위한 코딩 테스트다'의 문제입니다.
'''
N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다. 이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다. 예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개로 사용하는 것이 가장 최소한의 화폐 개수이다

입력 조건 :
첫째 줄에 N, M이 주어진다.(1 <= n <= 100, 1 <= M <= 10000)
이후 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐 가치는 10,000보다 작거나 같은 자연수이다

출력 조건 :
첫째 줄에 M원을 만들기 위한 최소한의 화폐 개수를 출력한다.
불가능할 때는 -1을 출력한다
'''
n, m = map(int, input().split())
d = [m+1] * (m+1)
money = []
for i in range(n) :
  money.append(int(input()))
  d[money[i]] = 1

i = max(money) + 1
for i in range(m+1) : #m원까지 쌓아간다. 
  for k in money :
    if d[i-k] > 0 :
      d[i] = min(d[i], d[i-k]+1)

if d[m] == 0 :
  print(-1)
else :
  print(d[m])

'''
#답안 예시
n, m = map(int, input().split())
array = []
for i in range(n) :
  array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n) :
  for j in range(array[i], m + 1) :
    if d[j-array[i]] != 10001 : 
      d[j] = min(d[j], d[j- array[i]] + 1)

if d[m] == 10001 :
  print(-1)
else :
  print(d[m])
'''
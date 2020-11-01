print('hello')
n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True)

result = 0;
count = 0
max_k  = 0
while count < m :
  if max_k < k :
    result += lst[0]
    max_k += 1
  else :
    result += lst[1]
    max_k = 0
  
  count += 1

print(result)


# 답안 예시
''''
n, m ,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
secont = data[n-2]

result = 0

while True :
  for i in range(k) :
    if m == 0 : 
      break
    result += first
    m -= 1
  if m == 0 :
    break;
  result += second
  m -= 1

print(result)
'''

'''
반복되는 수열에 대한 파악
반복되는 수열의 길이는? (k+1)
수열이 반복되는 횟수? m / (k+1)
m/(k+1)에다가 k를 곱해주면 큰 수가 등장하는 횟수가 된다.
최종식은 int(m/ (k + 1)) * k + M % (k +1)

n, m ,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

#아래 두 줄이 가장 큰 수가 등장하는 횟수다.
count =  int(m / (k+1))
count += m % (k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)
'''
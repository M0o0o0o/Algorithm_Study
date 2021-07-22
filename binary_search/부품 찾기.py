#해당 문제는 '이것이 취업을 위한 코딩 테스트다'의 문제입니다.
'''
동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며, 당일 날 견적서를 요청했다. 동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다. 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자. 
'''
def binary_search(parts, target, start, end) :
  while start <= end : 
    mid = (start + end) // 2
    if parts[mid] == target :
      return "yes"
    elif parts[mid] > target : 
      end = mid -1
    else :
      start = mid + 1
  
  return "no"


n = int(input())
parts = list(map(int,input().split()))
parts.sort()
m = int(input())
needs = list(map(int,input().split()))

for i in range(m) :
  print(binary_search(parts, needs[i], 0, n-1), end = ' ')



#집합 자료형 이용
n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int,input().split())) 

for i in x :
  if i in array :
    print('yes', end = ' ')
  else :
    print('no', end = ' ')
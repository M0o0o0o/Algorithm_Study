#해당 문제는 '이것이 취업을 위한 코딩 테스트다'의 문제입니다.
'''
오늘 동빈이는 여행 가싱 부모님을 대신해서 떡집 일을 하기로 했다. 오늘은 떡볶이 떡을 만드는 날이다. 동빈이네 떡볶이 떡은 재밌게도 떡의 길이가 일정하지 않다. 대신에 한 봉시 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
'''
def check(lst, height) :
  sum = 0
  for i in lst :
    if (i - height) > 0 :
      sum += (i - height)
  
  return sum

def binary(lst, m, start, end) :
  global result
  while start <= end : 
    mid = (start + end) // 2 
    sum = check(lst, mid)

    if sum == m : 
      result = mid
      break
    elif sum < m :
      end = mid - 1
    else : 
      # if result < sum : 
      #   result = sum 반복문을 넣을 필요가 없었다.
      result = sum 

      start = mid + 1


n, m = map(int, input().split())
lst = list(map(int,input().split()))
result = -1
binary(lst, m, min(lst), max(lst))

print(result) 



#답안 예시
n, m = list(map(int,input().split(' ')))
array = list(map(int,input().split()))

start = 0
end = max(array) 

# 이진 탐색 수행
result = 0
while(start <= end) :
  total = 0
  mid = (start + end) // 2
  #잘랐을 때의 떡의 양 계산
  for x in array :
    if x > mid :
      total += x - mid
  #떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
  if total < m :
    end = mid - 1
    #떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
  else :
    result = mid #최대한 덜 잘랏을 때가 정답이므로, 여기에서 result 기록 
    start = mid + 1

print(result) 
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end) :
  if start >= end : #원소가 1개인 경우 종료
    return 

  pivot = start #피벗은 첫 번째 원소 
  left = start + 1
  right = end

  while left <= right : 
#피벗보다 큰 데이터를 찾을 때까지 반복
#즉, 피벗값보다 작은 경우 탈출한다. 
    while left <= end and array[left] <= array[pivot]:
      left += 1
# 피벗보다 작은 데이터를 찾을 때까지 반복
    while right > start and array[right] >= array[pivot] :
      right -= 1
    if left > right :
      array[right], array[pivot] = array[pivot], array[right]
    else : 
      array[left], array[right] = array[right], array[left]
  
  quick_sort(array, start, right -1)
  quick_sort(array, right +1, end )

quick_sort(array,0, len(array) -1)

print(array)

'''
리스트의 첫 번째 데이터를 피벗으로 정한다(호어 분할)
피벗을 설정한 뒤에는 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서는 피벗보다 작은 데이터를 찾는다

왼쪽에서부터 찾는 값과 오른쪽에서 찾는 값의 위치가 서로 엇갈린다면, '작은 데이터'와 '피벗'의 위치를 서로 바꾼다.
(작은 값과 바꾸는 이유는 피벗을 기준으로 왼쪽은 피봇보다 작은 값들을 위치시키고(오름차순 기준), 오른쪽은 피봇보다 큰 값들을 위치시키기 위해서다.)
''''
